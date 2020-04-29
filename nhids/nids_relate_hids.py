#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time

#self own libraries
from redis_queue import DataInputRedis,ReadFromRedis
from log import log_decorator

def _utc2local(utc):
    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
    LOCAL_FORMAT = "%Y-%m-%d %H:%M:%S"
    utc_time = datetime.datetime.strptime(utc, UTC_FORMAT)
    local_time = utc_time + datetime.timedelta(hours=8)
    return local_time.strftime(LOCAL_FORMAT)

def _process_each_data(hids,nids_result):
    each_hids_result = []
    hids_data = hids["_source"]
    if hids_data.get("agent") != None and hids_data["agent"].get("ip") != None:
        hids_agent_ip = hids_data["agent"]["ip"]
    else:
        hids_agent_ip = None
    if hids_data.get("data") != None and hids_data["data"].get("srcip") != None:
        hids_srcip = hids_data["data"]["srcip"]
    else:
        hids_srcip = None

    for nids in nids_result:
        nids_data = nids["_source"]
        if nids_data.get("src_ip") != None:
            nids_src_ip = nids_data["src_ip"]

            '''judge if hids_srcip equal nids_src_ip first,if
            equal,continue,if not,then judge hids_anent_ip '''
            if hids_srcip == nids_src_ip:
                each_hids_result.append((hids_data,nids_data))
                continue
            if hids_agent_ip == nids_src_ip:
                each_hids_result.append((hids_data,nids_data))
                continue

        '''if hids_src_ip and hids_agent_ip not equal nids_src_ip,then 
        judge hids_agent_ip equal nids_dest_ip or not'''
        if nids_data.get("dest_ip") != None:
            nids_dest_ip = nids_data["dest_ip"]
            if hids_agent_ip == nids_dest_ip:
                each_hids_result.append((hids_data,nids_data))
    return each_hids_result


@log_decorator
def HidsRelateNids(hids_result,nids_result):
    nhids_result = []
    hids_count = 0
    DataInputRedis(hids_result,"hids_result")
    while True:
        each_data = ReadFromRedis("hids_result")

        hids_count +=1
        #every 100 times sleep 1s,reduce cpu pressure
        #if hids_count % 100 == 0:
        #    time.sleep(1)

        if each_data != None and isinstance(each_data,Exception) != True:
            each_hids_result = _process_each_data(each_data,nids_result)
            nhids_result += each_hids_result
        else:
            break
    return nhids_result
