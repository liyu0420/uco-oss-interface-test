import json
import unittest
import time
from common.configHttp import RunMain
import geturlParams
import urllib.parse
import readConfig as readConfig
import utils.Signature as Signature
import utils.JWTUtils as JWTUtils
import utils.S3 as s3


url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
readconfig = readConfig.ReadConfig()
bucketName = 'interfacetest'
objectName = 'logo.png'
ak = readconfig.get_params('accessKey')
sk = readconfig.get_params('secretKey')
endpoint = readconfig.get_params('endPoint')
openapiUrl = readconfig.get_http('openapiUrl')


class TestPresignedUrl(unittest.TestCase):
    def setUp(self):
        print("测试开始前准备")
        result = s3.create_bucket(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName)
        if result:
            print("桶创建成功")
        else:
            print("桶创建失败")
        result = s3.put_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName, object_name=objectName,
                               src_data=objectName)
        if result:
            print("文件上传成功")
        else:
            print("文件上传失败")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")
        result = s3.delete_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName, object_name=objectName)
        if result:
            print("文件删除成功")
        else:
            print("文件删除失败")
        result = s3.delete_bucket(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName)
        if result:
            print("桶删除成功")
        else:
            print("桶删除失败")

    def test_presignedUrl_forCdn(self):
        """
        生成预签名 for CDN
        """
        # 测试数据准备
        # baseUrl生成
        original_url = 'http://' + bucketName + '.' + endpoint + '/' + objectName
        base_url = Signature.url_base64(original_url)
        # Authorization 生成
        key = 'UnicloudSmaug'
        time_stamp = time.time()
        params = {
            'timeStamp': int(round(time_stamp * 1000))
        }
        token = JWTUtils.jwt_token(params=params, key=key)

        self.method = 'get'
        self.path = '/pco/v1/oss/presigned/covertToPresignedUrl'
        self.params = {
            'baseUrl': base_url,
            'expire': 2000
        }
        self.headers = {
            'Authorization': 'Bearer ' + token
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        print('signature : ' + signature)
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        print('预签名 ：' + ss['res'])
        self.assertEqual(ss['code'], '0')

    def test_presignedUrl_forCdn_openapi(self):
        """
        生成预签名 for CDN -openapi
        """
        # 测试数据准备
        # baseUrl生成
        original_url = 'http://' + bucketName + '.' + endpoint + '/' + objectName
        base_url = Signature.url_base64(original_url)
        # Authorization 生成
        key = 'UnicloudSmaug'
        time_stamp = time.time()
        params = {
            'timeStamp': int(round(time_stamp * 1000))
        }
        token = JWTUtils.jwt_token(params=params, key=key)

        self.method = 'get'
        self.path = '/pco/v1/oss/presigned/covertToPresignedUrl'
        self.params = {
            'baseUrl': base_url,
            'expire': 2000
        }
        self.headers = {
            'Authorization': 'Bearer ' + token
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        print('signature : ' + signature)
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = openapiUrl + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        print('预签名 ：' + ss['res'])
        self.assertEqual(ss['code'], '0')

    def test_user_url_openapi(self):
        """
        获取Iam认证
        """
        # 测试数据准备
        # baseUrl生成
        original_url = 'http://' + bucketName + '.' + endpoint + '/' + objectName
        base_url = Signature.url_base64(original_url)
        # Authorization 生成
        key = 'UnicloudSmaug'
        time_stamp = time.time()
        params = {
            'timeStamp': int(round(time_stamp * 1000))
        }
        token = JWTUtils.jwt_token(params=params, key=key)

        self.method = 'get'
        self.path = '/uos/oss'
        self.params = {
            'Action': 'covertToPresignedUrl',
            'baseUrl': base_url,
            'expire': 2000
        }
        self.headers = {
            'Authorization': 'Bearer ' + token
        }
        # 生成请求signature
        signature = Signature.sign(data=self.params,
                                   ak=readconfig.get_params('accessKey'),
                                   sk=readconfig.get_params('secretKey'),
                                   method='GET')
        print('signature : ' + signature)
        # 添加ak 与 signature 参数
        self.params.setdefault('AccessKeyId', readconfig.get_params('accessKey'))
        self.params.setdefault('Signature', urllib.parse.unquote(signature))  # python 会对参数自动进行编码，所以先进行解码

        new_url = openapiUrl + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_url(self):
        """
        获取Iam认证
        """
        # 测试数据准备
        # baseUrl生成
        original_url = 'http://' + bucketName + '.' + endpoint + '/' + objectName
        base_url = Signature.url_base64(original_url)
        # Authorization 生成
        key = 'UnicloudSmaug'
        time_stamp = time.time()
        params = {
            'timeStamp': int(round(time_stamp * 1000))
        }
        token = JWTUtils.jwt_token(params=params, key=key)

        self.method = 'get'
        self.path = '/oss'
        self.params = {
            'Action': 'covertToPresignedUrl',
            'baseUrl': base_url,
            'expire': 2000
        }
        self.headers = {
            'Authorization': 'Bearer ' + token,
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')


if __name__ == '__main__':
    print("iam测试")
