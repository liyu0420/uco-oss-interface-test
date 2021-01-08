import os
import configparser
import getpathInfo  # 引入我们自己的写的获取路径的类

path = getpathInfo.get_Path()  # 获取项目路径
config_path = os.path.join(path, 'config.ini')  # 获取配置项文件的路径
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_headers(self, name):
        value = config.get('HEADERS', name)
        return value

    def get_params(self, name):
        value = config.get('PARAMS', name)
        return value

    def get_cases(self,name):
        value = config.get('TESTCASE', name)
        return value


if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
    print('HEADERS：', ReadConfig().get_headers('uco-user-id'))
