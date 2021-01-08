import hashlib
import hmac
import base64
import urllib.parse

'''
@author liyu
@desc 生成signature
@date 2020/11/24
'''


# 生成signature
def sign(data=None, ak=None, sk=None, method=None):
    date_new = ''
    data.setdefault('AccessKeyId', ak)
    # 将参数排序并将value进行encode 并将参数使用&拼接
    for key, value in sorted(data.items()):
        date_new += key + '=' + urllib.parse.quote(str(value)) + "&"
    # 生成 sign_str
    sign_str = method + '&%2F&' + urllib.parse.quote(date_new.strip('&'))
    print(sign_str)
    # 生成签名
    hashing = hmac.new(bytes(sk + '&', encoding='utf-8'), bytes(sign_str, encoding='utf-8'),
                       hashlib.sha1).digest()
    signature = base64.b64encode(hashing).decode()
    return urllib.parse.quote(signature).replace('/', '%2F')


# base64加密
def url_base64(url):
    url_str = url.encode('utf-8')
    url_encode = base64.b64encode(url_str)
    res_url = str(url_encode, 'utf8')
    return res_url


if __name__ == '__main__':

    accessKeyId = 'c4ePPB7e3n92dqmx'
    secret = 'KJ8BXepRBQ8pDVIpcVejWvRy2Zjkpf'
    # 请求参数
    data = {
        'UserAccessKeyId': 'c4ePPB7e3n92dqmx'
    }
    method = 'GET'
    print('signature = ' + sign(data=data, ak=accessKeyId, sk=secret, method=method))

