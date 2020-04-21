#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime

#Third-party libraries
from elasticsearch import Elasticsearch,helpers
from apscheduler.schedulers.blocking import BlockingScheduler

#self own libraries
NIDS_BASE_DIR = \
os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(NIDS_BASE_DIR)
from log import *
from data_process import DataProcess
from conf import setting

es = Elasticsearch(['http://10.212.18.29:9200','http://10.212.21.60:9200'],http_auth=('elastic','abc123!@#'),
                   sniff_on_start=True,sniff_on_connection_fail=True,sniff_timeout=5)

def query_data(date):
    gte = "now-"+str(date)+"m"
    query_data = {
         "query": {
            "range": {
                "@timestamp": {
                    "gte": gte,
                    "lte": "now",
                    "format": "epoch_millis"
                }
            }
        }
    }
    #query_data = {
    #     "query": {
    #           "bool": {
    #               "must": [
    #                   {
    #                    "range": {
    #                        "timestamp": {
    #                            "gte": gte,
    #                            "lte": "now",
    #                            "format": "epoch_millis"
    #                        }
    #                    }
    #                }
    #            ]
    #        }
    #    }
    #}
    return query_data

def scroll_search(index='wazuh-alerts-3.x-*',doc_type="wazuh"):
    result = []
    scanResp = helpers.scan(es, query=query_data(setting.INTERVAL),doc_type=doc_type,
                            index=index, scroll= "1m")
    for hit in scanResp:
        result.append(hit)
    log.info("%s result is: %s"%(index,len(result)))
    return result

def process():
    hids_result = scroll_search(index="wazuh-alerts-3.x-*",doc_type="wazuh")
    nids_result = scroll_search(index="filebeat_suricata-*",doc_type="doc")
    DataProcess(hids_result,nids_result)

if __name__ == "__main__":

    #BlockingScheduler
    #sched = BlockingScheduler()
    #sched.add_job(process, 'interval', minutes=int(setting.INTERVAL))  # 每隔15分钟秒执行一次
    #sched.start()
    process()
