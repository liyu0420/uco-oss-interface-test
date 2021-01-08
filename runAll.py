import os
import unittest
from common import HTMLTestRunner
import getpathInfo


# 定义测试用例的目录为当前目录，跑所有的用例
path = getpathInfo.get_Path()
test_dir = os.path.join(path, 'testCase')
report_dir = os.path.join(path, 'result')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)


def run():
    print(discover)
    # 定义报告存放路径
    filename = os.path.join(report_dir, "report.html")

    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='OSS-CORE 接口测试报告')
    # 运行测试
    runner.run(discover)
    # 关闭报告文件
    fp.close()


if __name__ == "__main__":
   run()
