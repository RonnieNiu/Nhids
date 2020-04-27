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
from nids_relate_hids import DataProcess
from nhids_extract import extract
from conf import setting
from elastic_query import ScrollSearch

def process():
    hids_result = ScrollSearch(index="wazuh-alerts-3.x-*",doc_type="wazuh")
    nids_result = ScrollSearch(index="filebeat_suricata-*",doc_type="doc")
    nhids_result = DataProcess(hids_result,nids_result)
    extract(nhids_result)
if __name__ == "__main__":

    #BlockingScheduler
    #sched = BlockingScheduler()
    #sched.add_job(process, 'interval', minutes=int(setting.INTERVAL))  # 每隔15分钟秒执行一次
    #sched.start()
    process()
