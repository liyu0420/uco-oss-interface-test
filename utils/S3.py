import boto3
from botocore.exceptions import ClientError
import logging
import getpathInfo  # 自己定义的内部类，该类返回项目的绝对路径
# 拿到该项目所在的绝对路径
path = getpathInfo.get_Path()


def oss_client(ak=None, sk=None, endpoint=None):
    # noinspection PyUnusedLocal
    # noinspection PyShadowingNames
    oss_client = boto3.client(
        service_name='s3',
        aws_access_key_id=ak,
        aws_secret_access_key=sk,
        endpoint_url='http://' + endpoint,
        verify=False
    )
    return oss_client


def create_bucket(ak=None, sk=None, endpoint=None, bucket_name=None):
    try:
        client = oss_client(ak=ak, sk=sk, endpoint=endpoint)
        client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_bucket(ak=None, sk=None, endpoint=None, bucket_name=None):
    try:
        client = oss_client(ak=ak, sk=sk, endpoint=endpoint)
        client.delete_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def put_object(ak=None, sk=None, endpoint=None, bucket_name=None, object_name=None, src_data=None, ACL='private', StorageClass='STANDARD'):
    objectData = path + '/' + src_data
    if isinstance(objectData, bytes):
        object_data = objectData
    elif isinstance(objectData, str):
        try:
            object_data = open(objectData, 'rb')
            # possible FileNotFoundError/IOError exception
        except Exception as e:
            logging.error(e)
            return False
    else:
        return False

    try:
        client = oss_client(ak=ak, sk=sk, endpoint=endpoint)
        client.put_object(Bucket=bucket_name, Key=object_name, Body=object_data, ACL=ACL, StorageClass=StorageClass)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        if isinstance(src_data, str):
            object_data.close()
    return True


def object_exists(ak=None, sk=None, endpoint=None, bucket_name=None, object_name=None):
    try:
        client = oss_client(ak=ak, sk=sk, endpoint=endpoint)
        client.head_object(Bucket=bucket_name,Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_object(ak=None, sk=None, endpoint=None, bucket_name=None, object_name=None):
    if object_exists(ak=ak, sk=sk, endpoint=endpoint, bucket_name=bucket_name, object_name=object_name):
        try:
            client = oss_client(ak=ak, sk=sk, endpoint=endpoint)
            client.delete_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    return False
