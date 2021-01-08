import requests
import json
from common.Log import logger

logger = logger


class RunMain():

    def send_post(self, url, data, body, headers):  # 定义一个post方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        if not body:
            result = requests.post(url=url, params=data, headers=headers).json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
        else:
            result = requests.post(url=url, params=data, json=body, headers=headers).json()
        print("result:" + str(result))
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data, headers):
        result = requests.get(url=url, params=data, headers=headers).json()
        print("result:" + str(result))
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_put(self, url, data, body, headers):  # 定义一个put方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        if not body:
            result = requests.put(url=url, params=data, headers=headers).json()
        else:
            result = requests.put(url=url, params=data, json=body, headers=headers).json()
        print("result:" + str(result))
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_delete(self, url, data, headers):
        result = requests.delete(url=url, params=data, headers=headers).json()
        print("result:" + str(result))
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
    def run_main(self, method, url=None, data=None, body=None, headers=None):
        result = None
        if (method == 'post' or method == 'POST'):
            print("headers " + str(headers))
            print("params " + str(data))
            print("body: " + str(body))
            result = self.send_post(url, data, body, headers)
            logger.info(str(result))
        elif (method == 'get' or method == 'GET'):
            print("headers " + str(headers))
            print("params " + str(data))
            result = self.send_get(url, data, headers)
            logger.info(str(result))
        elif (method == 'delete' or method == 'DELETE'):
            print("headers " + str(headers))
            print("params " + str(data))
            result = self.send_delete(url, data, headers)
            logger.info(str(result))
        elif (method == 'put' or method == 'PUT'):
            print("headers " + str(headers))
            print("params " + str(data))
            print("body: " + str(body))
            result = self.send_put(url, data, body, headers)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=')
    print(result)
