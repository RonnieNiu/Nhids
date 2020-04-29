#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from elasticsearch import helpers

from log import log_decorator
from conf import setting
from elastic_conn import es

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
    return query_data

@log_decorator
def ScrollSearch(index='wazuh-alerts-3.x-*',doc_type="wazuh"):
    result = []
    try:
        scanResp = helpers.scan(es, query=query_data(setting.INTERVAL),doc_type=doc_type,
                            index=index, scroll= "1m")
        for hit in scanResp:
            result.append(hit)
        return result
    except Exception as e:
        return e


