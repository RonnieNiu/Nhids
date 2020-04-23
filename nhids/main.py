#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

#Third-party libraries
from apscheduler.schedulers.blocking import BlockingScheduler

#self own libraries
NIDS_BASE_DIR = \
os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(NIDS_BASE_DIR)
from data_process import DataProcess
from conf import setting
from elastic_query import ScrollSearch

def process():
    hids_result = ScrollSearch(index="wazuh-alerts-3.x-*",doc_type="wazuh")
    nids_result = ScrollSearch(index="filebeat_suricata-*",doc_type="doc")
    DataProcess(hids_result,nids_result)

if __name__ == "__main__":

    #BlockingScheduler
    #sched = BlockingScheduler()
    #sched.add_job(process, 'interval', minutes=int(setting.INTERVAL))  # 每隔15分钟秒执行一次
    #sched.start()
    process()
