import json
import unittest
from common.configHttp import RunMain
import geturlParams
import urllib.parse
import readConfig as readConfig
import utils.Signature as Signature

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
readconfig = readConfig.ReadConfig()
openapiUrl = readconfig.get_http('openapiUrl')


class TestIam(unittest.TestCase):
    def setUp(self):
        print("测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_user_getIamAndValidatedUser(self):
        """
        获取Iam认证
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/pco/v1/oss/iamValidation/access'
        self.params = {
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = url + self.path
        print(new_url)
        info = RunMain().run_main(self.method, url=new_url, data=self.params)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_iamAndValidatedUser(self):
        """
        获取Iam认证
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.params = {
            'Action': 'iamAndValidatedUser',
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_iamAndValidatedUser_openapi(self):
        """
        获取Iam认证-openapi
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/IamBlackUser/access'
        self.params = {
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = openapiUrl + self.path
        print(new_url)
        info = RunMain().run_main(self.method, url=new_url, data=self.params)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_openapi(self):
        """
        获取Iam认证-openapi
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/uos/oss'
        self.params = {
            'Action': 'iamAndValidatedUser',
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = openapiUrl + self.path
        print(new_url)
        info = RunMain().run_main(self.method, url=new_url, data=self.params)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_getIamAndValidatedChildUser(self):
        """
        获取子账号Iam认证
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/pco/v1/oss/iamValidation/access/info'
        self.params = {
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_iamAndValidatedChildUser(self):
        """
        获取Iam认证
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.params = {
            'Action': 'iamAndValidatedChildUser',
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_getIamAndValidatedChildUser_openapi(self):
        """
        获取子账号Iam认证-openapi
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss/IamBlackUser/access/info'
        self.params = {
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = openapiUrl + self.path
        print(new_url)
        info = RunMain().run_main(self.method, url=new_url, data=self.params)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_child_user_openapi(self):
        """
        获取Iam认证-openapi
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/uos/oss'
        self.params = {
            'Action': 'iamAndValidatedChildUser',
            'UserAccessKeyId': readconfig.get_params('accessKey')
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = openapiUrl + self.path
        print(new_url)
        info = RunMain().run_main(self.method, url=new_url, data=self.params)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_getchildUserbyParentId(self):
        """
        获取主账号下子账号列表
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getchildUserbyParentId',
            'parentId': readconfig.get_headers('uco-user-id')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def todo_test_user_getTemporaryAccess(self):
        """
        获取临时aksk
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getTemporaryAccess',
            'regionId': readconfig.get_params('regionId')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')


if __name__ == '__main__':
    print("iam测试")
