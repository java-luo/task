from redis import *


def get(key):
    redis = StrictRedis()
    value = redis.get(key)
    redis.close()
    return value


def set(key, value, ex=None):
    redis = StrictRedis()
    rtn=redis.set(key, value,ex)
    redis.close()
    return rtn


