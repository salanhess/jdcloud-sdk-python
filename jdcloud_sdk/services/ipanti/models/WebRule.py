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
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class WebRule(object):

    def __init__(self, webRuleId=None, domain=None, cname=None, protocol=None, port=None, originType=None, originAddr=None, httpsCertContent=None, httpsRsaKey=None, httpCertStatus=None, status=None, ccStatus=None):
        """
        :param webRuleId: (Optional) 规则id
        :param domain: (Optional) 子域名
        :param cname: (Optional) 规则的cname
        :param protocol: (Optional) 协议：HTTP、HTTPS、HTTP_HTTPS
        :param port: (Optional) 端口号，80,443
        :param originType: (Optional) 回源类型：ip或者domain
        :param originAddr: (Optional) 回源地址：originType为ip时为多个填多个ip，originType为domain时填一个域名
        :param httpsCertContent: (Optional) 证书内容
        :param httpsRsaKey: (Optional) 证书私钥
        :param httpCertStatus: (Optional) 证书状态：0异常，1正常
        :param status: (Optional) 0防御状态，1回源状态
        :param ccStatus: (Optional) 0CC关闭 1CC开启
        """

        self.webRuleId = webRuleId
        self.domain = domain
        self.cname = cname
        self.protocol = protocol
        self.port = port
        self.originType = originType
        self.originAddr = originAddr
        self.httpsCertContent = httpsCertContent
        self.httpsRsaKey = httpsRsaKey
        self.httpCertStatus = httpCertStatus
        self.status = status
        self.ccStatus = ccStatus