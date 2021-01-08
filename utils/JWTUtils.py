import time
import jwt


def jwt_token(params = None,key = None):
    # headers
    headers = {
        'alg': 'HS256',  # 声明所使用的算法
        'typ': 'JWT'
    }

    # 调用jwt库,生成json web token
    jwt_token = jwt.encode(params,  # payload, 有效载体
                           key,  # 进行加密签名的密钥
                           algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                           headers=headers  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                           ).decode('ascii')  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str

    print(jwt_token)
    return jwt_token


if __name__ == '__main__':

    # 请求参数
    params = {
        'timeStamp': time.time()
    }
    key = 'UnicloudSmaug'
    print('token = ' + jwt_token(params=params, key=key))
