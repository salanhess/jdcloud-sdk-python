# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import traceback
import requests
import base64
from jdcloud_sdk.core import const
from jdcloud_sdk.core.signer import Signer
from jdcloud_sdk.core.version import version
from jdcloud_sdk.core.parameterbuilder import WithBodyBuilder, WithoutBodyBuilder
from jdcloud_sdk.core.exception import ClientException
from jdcloud_sdk.core.jdcloudresponse import JDCloudResponse, ErrorResponse
from jdcloud_sdk.core.logger import get_default_logger, INFO, ERROR


class JDCloudClient(object):

    def __init__(self, credential, config, service_name, revision, logger):
        self.__config = config
        self.__service_name = service_name
        self.__credential = credential
        self.__revision = revision
        self.__logger = logger

        if logger is None:
            self.__logger = get_default_logger()

        self.__builder_map = {const.METHOD_GET: WithoutBodyBuilder,
                              const.METHOD_DELETE: WithoutBodyBuilder,
                              const.METHOD_HEAD: WithoutBodyBuilder,
                              const.METHOD_PUT: WithBodyBuilder,
                              const.METHOD_POST: WithBodyBuilder,
                              const.METHOD_PATCH: WithBodyBuilder}

    def send(self, request):
        if self.__config is None:
            raise ClientException('Miss config object')
        if self.__credential is None:
            raise ClientException('Miss credential object')
        if request is None:
            raise ClientException('Miss request object')
        if request.parameters is None:
            raise ClientException('Miss parameters in request')

        region = self.__get_region_id(request)

        try:
            header = self.__merge_headers(request.header)
            param_builder = self.__builder_map[request.method]()
            url = param_builder.build_url(request, self.__config.scheme, self.__config.endpoint)
            body = param_builder.build_body(request)
            self.__logger.log(INFO, 'url=' + url)
            self.__logger.log(INFO, 'body=' + body)

            signer = Signer(self.__logger)
            signer.sign(method=request.method, region=region, uri=url,
                        headers=header, data=body, credential=self.__credential,
                        security_token="", service=self.__service_name)
            self.__logger.log(INFO, header)

            resp = requests.request(request.method, url, data=body, headers=header,
                                    timeout=self.__config.timeout)
            self.__logger.log(INFO, resp.content)

            return self.__process_response(request.method, resp)
        except Exception as e:
            msg = traceback.format_exc()
            self.__logger.log(ERROR, msg)
            raise e

    def __merge_headers(self, request_header):
        header = dict()
        header['User-Agent'] = 'JdcloudSdkPython/%s %s/%s' % (version, self.__service_name, self.__revision)
        header['Content-Type'] = 'application/json'

        if request_header is not None:
            for k, v in request_header.items():
                if k.lower().startswith(const.HEADER_JDCLOUD_PREFIX)\
                        or k.lower().startswith(const.HEADER_JCLOUD_PREFIX):
                    v = base64.b64encode(v)
                header[k] = v

        self.__logger.log(INFO, header)
        return header

    def __get_region_id(self, request):
        if not hasattr(request.parameters, 'regionId') or request.parameters.regionId is None:
            return 'jdcloud-api'  # when no region, use this value to fill field for sign

        return request.parameters.regionId

    def __process_response(self, method, response):
        jd_resp = JDCloudResponse()

        if method == const.METHOD_HEAD:
            request_id = response.headers.get(const.HEADER_REQUESTID)
            if request_id is None or request_id == '':
                jd_resp.error = ErrorResponse('', '500', 'can not get requestId in HEAD response')
                jd_resp.requestId = ''
            else:
                jd_resp.requestId = request_id
        else:
            jd_resp.fill_value(response.content)

        return jd_resp
