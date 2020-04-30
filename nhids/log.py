#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import TimedRotatingFileHandler

from functools import wraps

from conf import setting

log_path = setting.LOGPATH
if not os.path.exists(log_path):
    try:
        os.mkdir(log_path)
    except:
        os.makedirs(log_path)

log = logging.getLogger('ybn')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s: %(levelname)s:%(message)s")
log_file_handler = \
        TimedRotatingFileHandler(filename=os.path.join(log_path,"run"),when="MIDNIGHT",interval=1)
log_file_handler.setFormatter(formatter)
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.suffix = "%Y-%m-%d.log"
log.addHandler(log_file_handler)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args,**kv):
        result = func(*args,**kv)
        if isinstance(result,Exception) == True:
            log.error("%s: %s"%(func.__name__,result))
        elif func.__name__ == "ScrollSearch":
            if kv.get("index") != None:
                log.info("%s: %s result is: %s"%(func.__name__,kv["index"],len(result)))
        elif func.__name__ == "HidsRelateNids":
            log.info("%s: the nhids num is: %d"%(func.__name__,len(result)))
        elif func.__name__ == "WriteInputElastic":
            log.info("%s: sucess write input elastic: %d\n"%(func.__name__,result))
        return result
    return wrapper
