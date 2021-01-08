import json
import unittest
from common.configHttp import RunMain
import geturlParams
import readConfig as readConfig
import time
import datetime

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
readconfig = readConfig.ReadConfig()


class TestProduct(unittest.TestCase):
    def setUp(self):
        print("测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_order_getProduct(self):
        """
        获取对象售卖项
        """
        print("getProduct")
        # 接口数据准备
        self.method = 'post'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getProducts'
        }
        self.body = {
            'userId': readconfig.get_headers('uco-user-id'),
            'componentCodes': ['OSS', 'OSSDATA', 'OSSAPI'],
            'regionId': readconfig.get_params('regionId'),
            'paymentMethodCode': 'YEAR_MONTH',
            'operationAbility': 'NEW'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers, body=self.body)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_getProductPurchaseTime(self):
        """
        获取产品可售卖时长
        """
        print("getProductPurchaseTime")
        # 接口数据准备
        self.method = 'post'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getProductPurchaseTime'
        }
        self.body = [
            'OSSAPI',
            'OSS',
            'OSSDATA'
        ]

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers, body=self.body)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_getProductPaymentByUserAndRegion(self):
        """
        获取用户可用计费方式
        """
        print("getProductPaymentByUserAndRegion")
        # 接口数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getProductPaymentByUserAndRegion',
            'regionId': readconfig.get_params('regionId'),
            'productCode': 'OSS'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_getResourceList(self):
        """
        获取有效资源包列表
        """
        print("getResourceList")
        # 接口数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getResourceList',
            'regionId': readconfig.get_params('regionId'),
            'page': '1',
            'size': '10'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_getExpiredResourceList(self):
        """
        获取过期资源包列表
        """
        print("getExpiredResourceList")
        # 接口数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getExpiredResourceList',
            'regionId': readconfig.get_params('regionId'),
            'page': '1',
            'size': '10'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_getUsageDetails(self):
        """
        获取资源包使用明细
        """
        print("getUsageDetails")
        # 接口数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getUsageDetails',
            'regionId': readconfig.get_params('regionId'),
            'page': '1',
            'size': '10',
            # 'orderId': '1',
            # 'resourcePackType': 'STANDARD',
            # 'deductProduct': 'OSS'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_getInstance(self):
        """
        获取实例信息
        """
        print("getInstance")
        # 接口数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getInstance',
            'instanceIds': readconfig.get_headers('uco-user-id')
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_order_pullPostPayUsages(self):
        """
        运营平台拉量接口
        """
        print("pullPostPayUsages")
        a = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % 1
        time_array = time.strptime(a, "%Y-%m-%d %H:%M:%S")
        hour_stamp = int(time.mktime(time_array))
        next_hour = hour_stamp + 3600
        print(hour_stamp)
        # 接口数据准备
        self.method = 'post'
        self.path = '/v1/oss/order/pullPostPayUsages'
        self.params = {}
        self.body = {
            'regionId': '*',
            'startTime': hour_stamp*1000,
            'endTime': next_hour*1000,
            'instanceIds': [
                readconfig.get_headers('uco-user-id')
            ]
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, body=self.body)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['status'], True)


if __name__ == '__main__':
    print("配置项测试")
