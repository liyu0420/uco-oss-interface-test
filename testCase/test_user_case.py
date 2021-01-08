import json
import unittest
from common.configHttp import RunMain
import geturlParams
import readConfig as readConfig

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
readconfig = readConfig.ReadConfig()


class TestUser(unittest.TestCase):
    def setUp(self):
        print("测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_user_getOpenstate(self):
        """
        获取用户开通状态
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getOpenState'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')

    def test_user_getStatus(self):
        """
        获取对象存储用户状态
        """
        # 测试数据准备
        self.method = 'get'
        self.path = '/oss'
        self.headers = {
            'uco-user-id': readconfig.get_headers('uco-user-id'),
            'uco-user-name': readconfig.get_headers('uco-user-name')
        }
        self.params = {
            'Action': 'getUserStatus'
        }

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, data=self.params, headers=self.headers)
        ss = json.loads(info)  # 将响应转换为字典格式
        self.assertEqual(ss['code'], '0')


if __name__ == '__main__':
    print("用户测试")
