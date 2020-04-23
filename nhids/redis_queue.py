#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
import json
import time

from log import log_decorator
from conf import setting

pool = redis.ConnectionPool(host=setting.REDIS_HOST, port=setting.REDIS_PORT,
                            password=setting.REDIS_AUTH, db=setting.REDIS_DB, decode_responses=True)
redis_conn = redis.Redis(connection_pool=pool)

#read from redis
@log_decorator
def ReadFromRedis(redis_key):
    try:
        each_data = redis_conn.blpop(redis_key, timeout=1)
        if each_data != None:
            return json.loads(each_data[1])
        return each_data
    except Exception as e:
        return e

@log_decorator
def DataInputRedis(result_list,redis_key):
    for each_data in result_list:
        each_data = json.dumps(each_data)
        try:
            res = redis_conn.rpush(redis_key,each_data)
        except Exception as e:
            time.sleep(60)
            return e
    return None
