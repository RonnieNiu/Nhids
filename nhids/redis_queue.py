#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
import json
import time

from log import *

pool = redis.ConnectionPool(host="10.212.18.29", port=6390, password="abc123!@#", db=0, decode_responses=True)
redis_conn = redis.Redis(connection_pool=pool)

#read from redis
def ReadFromRedis(redis_key):
    try:
        each_data = redis_conn.blpop(redis_key, timeout=1)
        if each_data != None:
            return json.loads(each_data[1])
        return each_data
    except Exception as e:
        log.error("read_from_redis error: %s" %e)
        return None

def DataInputRedis(result_list,redis_key):
    for each_data in result_list:
        each_data = json.dumps(each_data)
        try:
            res = redis_conn.rpush(redis_key,each_data)
        except Exception as e:
            log.error("data_input_redis error:%s" %e)
            time.sleep(60)

