import json
import unittest
from common.configHttp import RunMain
import geturlParams
import readConfig as readConfig
import utils.S3 as s3
import time

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
readconfig = readConfig.ReadConfig()
bucketName = 'interfacetest'
objectName = 'logo.png'
ak = readconfig.get_params('accessKey')
sk = readconfig.get_params('secretKey')
endpoint = readconfig.get_params('endPoint')


class TestOssBucket(unittest.TestCase):
    def setUp(self):
        print("测试开始前准备")
        result = s3.create_bucket(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName)
        if result:
            print("桶创建成功")
        else:
            print("桶创建失败")
        result = s3.put_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName, object_name=objectName, src_data=objectName)
        if result:
            print("文件上传成功")
        else:
            print("文件上传失败")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")
        result = s3.delete_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName,object_name=objectName)
        if result:
            print("文件删除成功")
        else:
            print("文件删除失败")
        result = s3.delete_bucket(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName)
        if result:
            print("桶删除成功")
        else:
            print("桶删除失败")

    def test_accessList(self):
        """
        获取accessKey
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'accessList'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_objectHead_test(self):
        """
        获取对象解冻状态
        """
        objectKey = 'logo1.png'
        result = s3.put_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName, object_name=objectKey,
                               src_data=objectName, StorageClass='GLACIER')
        if result:
            print("文件上传成功")
        else:
            print("文件上传失败")
        # 测试数据准备

        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'headObject',
            'bucketName': bucketName,
            'endpoint': endpoint,
            'objectName': objectKey,
            # 'versionId': ''  # versionId非必须参数
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')
        result = s3.delete_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName, object_name=objectKey)
        if result:
            print("文件删除成功")
        else:
            print("文件删除失败")

    def test_getObejectMetadata(self):
        """
        获取对象HTTP头信息
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getObejectMetadata',
            'bucketName': bucketName,
            'objectName': objectName,
            'regionId': readconfig.get_params('regionId'),
            # 'versionId': ''  # versionId非必须参数
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_presignedUrl_getUrl(self):
        """
        生成预签名
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getPresignedUrl',
            'requestType': 'GET',
            'bucketName': bucketName,
            'objectKey': objectName,
            'regionId': readconfig.get_params('regionId'),
            'expire': 2000,
            'directDownload': False
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        print('预签名 ：' + ss['res']['url'])
        self.assertEqual(ss['code'], '0')

    def test_objectRename_test(self):
        """
        修改对象名称
        """
        # 测试数据准备
        self.method = 'put'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'renameObject'
        }
        self.body = {
            'bucketName': bucketName,
            'regionId': readconfig.get_params('regionId'),
            'destinationKey': 'logo2.png',
            'sourceKey': objectName
            # 'versionId': ''  # versionId非必须参数
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, body= self.body, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

        time.sleep(3)

        self.body = {
            'bucketName': bucketName,
            'regionId': readconfig.get_params('regionId'),
            'destinationKey': 'logo3.png',
            'sourceKey': 'logo2.png'
            # 'versionId': ''  # versionId非必须参数
        }
        info = RunMain().run_main(self.method, url=new_url, data=self.params, body=self.body, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

        result = s3.delete_object(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucketName, object_name='logo3.png')
        if result:
            print("文件删除成功")
        else:
            print("文件删除失败")

    def test_imageStyle(self):
        """
        图片样式
        """
        # # 添加
        # self.method = 'post'
        # self.path = '/oss'
        # self.headers = {
        #     'uco-user-id': readconfig.get_headers('uco-user-id'),
        #     'uco-user-name': readconfig.get_headers('uco-user-name')
        # }
        # self.params = {
        #     'Action': 'setImagestyle'
        # }
        # self.body = {
        #     'styleCode': 'image/rotate,17',
        #     'styleName': 'liyutest1126',
        #     'bucketName': bucketName,
        #     'bucketDomain': bucketName + '.' + endpoint,
        #
        # }
        # new_url = url + self.path
        # info = RunMain().run_main(self.method, url=new_url, data=self.params, body=self.body, headers=self.headers)
        # ss = json.loads(info)  # 将响应转换为字典格式
        # self.assertEqual(ss['code'], '0')
        #
        # # 修改
        # # 测试数据准备
        # self.method = 'post'
        # self.path = '/oss'
        # self.headers = {
        #     'uco-user-id': readconfig.get_headers('uco-user-id'),
        #     'uco-user-name': readconfig.get_headers('uco-user-name')
        # }
        # self.params = {
        #     'Action': 'resetImageStyle'
        # }
        # self.body = {
        #     'styleCode': 'image/rotate,12/resize,m_lfit,h_401,limit_0',
        #     'styleName': 'liyutest11261559',
        #     'bucketName': bucketName,
        #     'bucketDomain': bucketName + '.' + endpoint,
        #
        # }
        # new_url = url + self.path
        # info = RunMain().run_main(self.method, url=new_url, data=self.params, body=self.body, headers=self.headers)
        # ss = json.loads(info)  # 将响应转换为字典格式
        # self.assertEqual(ss['code'], '0')

        # 获取
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getImageStyle',
            'page': '1',
            'size': '10',
            'bucketName': bucketName,
            'bucketDomain': bucketName + '.' + endpoint
        }
        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

        # # 删除
        # # 测试数据准备
        # self.method = 'delete'
        # self.path = '/oss'
        # self.headers = {
        #     'uco-user-id': readconfig.get_headers('uco-user-id'),
        #     'uco-user-name': readconfig.get_headers('uco-user-name')
        # }
        # self.params = {
        #     'Action': 'delImageStyle',
        #     "styleNames": ['liyutest11261559'],
        #     'bucketName': bucketName,
        #     'bucketDomain': bucketName + '.' + endpoint
        # }
        # new_url = url + self.path
        # info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        # ss = json.loads(info)  # 将响应转换为字典格式
        # self.assertEqual(ss['code'], '0')

    def test_customdomain_get(self):
        """
        获取自定义域名
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getCustomdomain',
            'endpoint': endpoint,
            'bucketDomain': bucketName + '.' + endpoint
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def todo_test_customdomain_set(self):
        """
        设置自定义域名
        """
        # 测试数据准备
        self.method = 'put'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getCustomdomain'
        }
        self.body = {
            'endpoint': 's3.test.com',
            'bucketDomain': 'liyutest77.s3.test.com',
            'hostDomain': '',
            'bucketName': ''
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers, body=self.body)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def todo_test_customdomain_del(self):
        """
        删除自定义域名
        """
        # 测试数据准备
        self.method = 'delete'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'delCustomdomain',
            'endpoint': 's3.test.com',
            'hostDomain': ''
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def todo_test_certificate_put(self):
        """
        上传用户证书
        """
        # 测试数据准备
        self.method = 'post'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'putCertificate'
        }
        self.body = {
            'host_domain': '',
            'bucketName': '',
            'endpoint': '',
            'bucketDomain': '',
            'tls_domain': '',
            'tls_domain_key': ''
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, body=self.body, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def todo_test_certificate_del(self):
        """
        删除用户证书
        """
        # 测试数据准备
        self.method = 'delete'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'delCertificate',
            'host_domain': '',
            'endpoint': '',
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params,  headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')


if __name__ == '__main__':
    print("配置项测试")
