# 简介 #
  欢迎使用京东云开发者Python工具套件（Python SDK）。使用京东云Python SDK，您无需复杂编程就可以访问京东云提供的各种服务。 

  为了方便您理解SDK中的一些概念和参数的含义，使用SDK前建议您先查看OpenAPI使用入门。要了解每个API的具体参数和含义，请参考程序注释或参考OpenAPI&SDK下具体产品线的API文档。

# 环境准备 #

1. 京东云Python SDK适用于Python 2.7.*及以上版本，暂未支持3.*版本。
2. 在开始调用京东云open API之前，需提前在京东云用户中心账户管理下的AccessKey管理页面申请accesskey和secretKey密钥对（简称AK/SK）。AK/SK信息请妥善保管，如果遗失可能会造成非法用户使用此信息操作您在云上的资源，给你造成数据和财产损失。

# SDK使用方法 #
建议使用pip安装京东云Python SDK，如下所示：

	pip install jdcloud_sdk
您还可以下载sdk源代码自行使用。

使用源码安装您可以如下方式执行：

	python setup.py install
 
SDK使用中的任何问题，欢迎您在Issues页面交流。

**注意：京东云并没有提供其他下载方式，请务必使用上述官方下载方式！**
 
调用SDK
Python SDK的调用主要分为4步：

1. 设置accessKey和secretKey
2. 创建Client
3. 设置请求参数
4. 执行请求得到响应

以下是查询云主机实例类型的调用示例

```python
access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
credential = Credential(access_key, secret_key)
client = VmClient(credential)

parameters = DescribeInstanceTypesParameters('cn-north-1')
request = DescribeInstanceTypesRequest(parameters)
resp = client.send(request)
print resp
```    

