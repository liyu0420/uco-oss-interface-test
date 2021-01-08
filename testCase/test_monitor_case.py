import json
import unittest
from common.configHttp import RunMain
import geturlParams
import readConfig as readConfig
import utils.Signature as Signature
import urllib.parse

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
readconfig = readConfig.ReadConfig()


class TestMonitor(unittest.TestCase):
    def setUp(self):
        print("测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_user_month_statistics(self):
        """
        用户30天内api/流量使用量情况
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'month_statistics',
            'cloudId': readconfig.get_params('regionId'),
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_month_statistics(self):
        """
        桶30天内api/流量使用量情况
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'month_statistics',
            'cloudId': readconfig.get_params('regionId'),
            'bucketName': 'liyutest77'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_usage_all(self):
        """
        用户当前存储量
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'bucket_usage_all',
            'regionId': readconfig.get_params('regionId'),
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_usage(self):
        """
        桶当前存储量
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'bucket_usage_all',
            'regionId': readconfig.get_params('regionId'),
            'bucketName': 'liyutest77'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_object_num(self):
        """
        用户桶数量及对象数量
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'bucket_object_num',
            'regionId': readconfig.get_params('regionId'),
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_object_num(self):
        """
        桶内对象数量
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'bucket_object_num',
            'regionId': readconfig.get_params('regionId'),
            'bucketName': 'liyutest77'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_getUsageByTime(self):
        """
        用户存储使用量随时间变化
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getUsageByTime',
            'cloudId': readconfig.get_params('regionId'),
            'date': 'today'  # {pastMonth,pastWeek,today}
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_getUsageByTime(self):
        """
        桶内存储使用量随时间变化
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getUsageByTime',
            'cloudId': readconfig.get_params('regionId'),
            'date': 'today',  # {pastMonth,pastWeek,today}
            'bucketName': 'liyutest77'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_getFlowByTime(self):
        """
        用户流量随时间变化
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getFlowByTime',
            'cloudId': readconfig.get_params('regionId'),
            'date': 'today',  # {pastMonth,pastWeek,today}
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_getFlowByTime(self):
        """
        桶流量随时间变化
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getFlowByTime',
            'cloudId': readconfig.get_params('regionId'),
            'date': 'today',  # {pastMonth,pastWeek,today}
            'bucketName': 'liyutest77'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_getApiByTime(self):
        """
        用户API随时间变化
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getApiByTime',
            'cloudId': readconfig.get_params('regionId'),
            'date': 'today'  # {pastMonth,pastWeek,today}
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_bucket_getApiByTime(self):
        """
        桶API随时间变化
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getApiByTime',
            'cloudId': readconfig.get_params('regionId'),
            'date': 'today',  # {pastMonth,pastWeek,today}
            'bucketName': 'liyutest77'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_getEndpointByRegionId(self):
        """
        根据regionId 获取 endpoint
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getEndpointByRegionId',
            'cloudId': readconfig.get_params('regionId'),
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_getEndpoint(self):
        """
        获取用户所有可用地域
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getEndpoint'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_region_getEndpoint(self):
        """
        获取某地域信息
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getEndpoint',
            'regionId': readconfig.get_params('regionId')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_region_endpoint(self):
        """
        获取某地域信息
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/pco/v1/oss/overview/getEndpoint'
        self.params = {
            'regionId': readconfig.get_params('regionId')
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


if __name__ == '__main__':
    print("配置项测试")
