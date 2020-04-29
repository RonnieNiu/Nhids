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
from nids_relate_hids import HidsRelateNids
from nhids_extract import extract
from conf import setting
from elastic_query import ScrollSearch
from elastic_write import WriteInputElastic

def process():
    #search hids and nids alert events from elastic
    hids_result = ScrollSearch(index="wazuh-alerts-3.x-*",doc_type="wazuh")
    nids_result = ScrollSearch(index="filebeat_suricata-*",doc_type="doc")

    #relate hids and nids events
    nhids_result = HidsRelateNids(hids_result,nids_result)
    
    #extract nhids events,generate the final events
    final_events = extract(nhids_result)

    #write final_events to elastic
    WriteInputElastic(final_events)

if __name__ == "__main__":

    #BlockingScheduler
    #sched = BlockingScheduler()
    #sched.add_job(process, 'interval', minutes=int(setting.INTERVAL))  # 每隔15分钟秒执行一次
    #sched.start()
    process()
