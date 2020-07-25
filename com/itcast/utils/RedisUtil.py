from redis import *

from com.itcast.utils import iniUtil

redis_host = iniUtil.getInI("redis", "ip")
redis_port = iniUtil.getInI("redis", "port")


def get(key):
    redis = StrictRedis(host=redis_host, port=redis_port)
    value = redis.get(key)
    redis.close()
    return value


def set(key, value, ex=None):
    redis = StrictRedis(host=redis_host, port=redis_port)
    rtn = redis.set(key, value, ex)
    redis.close()
    return rtn
