#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import TimedRotatingFileHandler

from conf import setting

log_path = setting.LOGPATH
if not os.path.exists(log_path):
    try:
        os.mkdir(log_path)
    except:
        os.makedirs(log_path)

log = logging.getLogger('ybn')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s: %(filename)s[第%(lineno)d行]: %(levelname)s:%(message)s")
log_file_handler = \
        TimedRotatingFileHandler(filename=os.path.join(log_path,"run"),when="MIDNIGHT",interval=1)
log_file_handler.setFormatter(formatter)
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.suffix = "%Y-%m-%d.log"
log.addHandler(log_file_handler)

