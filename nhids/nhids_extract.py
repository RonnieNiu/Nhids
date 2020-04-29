#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def _hids_extract(hids):
    ##############################################################################
    if hids.get("agent") != None and hids["agent"].get("ip") != None:
        hids_agent_ip = hids["agent"]["ip"]
    else:
        hids_agent_ip = "null"
    ##############################################################################
    if hids.get("data") != None and hids["data"].get("srcip") != None:
        hids_srcip = hids["data"]["srcip"]
    else:
        hids_srcip = "null"

    if hids.get("data") != None and hids["data"].get("srcport") != None:
        hids_srcport = hids["data"]["srcport"]
    else:
        hids_srcport = "null"
    ##############################################################################
    if hids.get("full_log") != None:
        hids_full_log = hids["full_log"]
    else:
        hids_full_log = "null"
    ##############################################################################
    if hids.get("cluster") != None and hids["cluster"].get("node"):
        hids_node = hids["cluster"]["node"]
    else:
        hids_node = "null"
    ##############################################################################
    if hids.get("rule") != None and hids["rule"].get("description") != None:
        hids_rule_description = hids["rule"]["description"]
    else:
        hids_rule_description = "null"

    if hids.get("rule") != None and hids["rule"].get("level") != None:
        hids_rule_level = hids["rule"]["level"]
    else:
        hids_rule_level = "null"
    ##############################################################################
    if hids.get("@timestamp") != None:
        hids_timestamp = hids["@timestamp"]
    else:
        hids_timestamp = "null"
    ##############################################################################
    '''
    print("hids_agent_ip: %s"%hids_agent_ip)
    print("hids_srcip: %s"%hids_srcip)
    print("hids_srcport: %s"%hids_srcport)
    print("hids_node； %s"%hids_node)
    print("hids_rule_description: %s"%hids_rule_description)
    print("hids_rule_level: %s"%hids_rule_level)
    print("hids_full_log: %s"%hids_full_log)
    print("hids_timestamp: %s"%hids_timestamp)
    print("##########################################################")
    '''
    return [("hids_agent_ip",hids_agent_ip),("hids_srcip",hids_srcip),\
            ("hids_srcport",hids_srcport),("hids_node",hids_node),\
            ("hids_rule_description",hids_rule_description),("hids_rule_level",hids_rule_level),\
            ("hids_full_log",hids_full_log),("hids_timestamp",hids_timestamp)]

def _nids_extract(nids):
    #######################################################################
    if nids.get("alert") != None and nids["alert"].get("action") != None:
        nids_action = nids["alert"]["action"]
    else:
        nids_action = "null"

    if nids.get("alert") != None and nids["alert"].get("category") != None:
        nids_category = nids["alert"]["category"]
    else:
        nids_category = "null"

    if nids.get("alert") != None and nids["alert"].get("signature") != None:
        nids_signature = nids["alert"]["signature"]
    else:
        nids_signature = "null"
   ###########################################################################
    if nids.get("dest_host") != None:
        nids_dest_host = nids["dest_host"]
    else:
        nids_dest_host = "null"

    if nids.get("dest_ip") != None:
        nids_dest_ip = nids["dest_ip"]
    else:
        nids_dest_ip = "null"

    if nids.get("dest_port") != None:
        nids_dest_port = nids["dest_port"]
    else:
        nids_dest_port = "null"

    if nids.get("dest_project") != None:
        nids_dest_project = nids["dest_project"]
    else:
        nids_dest_project = "null"

    if nids.get("dest_service") != None:
        nids_dest_service = nids["dest_service"]
    else:
        nids_dest_service = "null"

    if nids.get("dest_user") != None:
        nids_dest_user = nids["dest_user"]
    else:
        nids_dest_user = "null"
    ########################################################################
    if nids.get("src_host") != None:
        nids_src_host = nids["src_host"]
    else:
        nids_src_host = "null"

    if nids.get("src_ip") != None:
        nids_src_ip = nids["src_ip"]
    else:
        nids_src_ip = "null"

    if nids.get("src_port") != None:
        nids_src_port = nids["src_port"]
    else:
        nids_src_port = "null"

    if nids.get("src_project") != None:
        nids_src_project = nids["src_project"]
    else:
        nids_src_project = "null"

    if nids.get("src_service") != None:
        nids_src_service = nids["src_service"]
    else:
        nids_src_service = "null"

    if nids.get("src_user") != None:
        nids_src_user = nids["src_user"]
    else:
        nids_src_user = "null"
    ########################################################################
    if nids.get("payload") != None:
        nids_payload = nids["payload"]
    else:
        nids_payload = "null"
 
    if nids.get("payload_printable") != None:
        nids_payload_printable = nids["payload_printable"]
    else:
        nids_payload_printable = "null"
   #####################################################################
    if nids.get("log") != None and nids["log"].get("file") != None and\
    nids["log"]["file"]["path"]:
        nids_log_file_path = nids["log"]["file"]["path"]
    else:
        nids_log_file_path = "null"
    ##################################################################
    if nids.get("@timestamp") != None:
        nids_timestamp = nids["@timestamp"]
    else:
        nids_timestamp = "null"
    '''
    print(nids_action)
    print(nids_category)
    print(nids_signature)
    print(nids_dest_host)
    print(nids_dest_ip)
    print(nids_dest_port)
    print(nids_dest_project)
    print(nids_dest_service)
    print(nids_dest_user)
    print(nids_src_host)
    print(nids_src_ip)
    print(nids_src_port)
    print(nids_src_project)
    print(nids_src_service)
    print(nids_src_user)
    print(nids_payload)
    print(nids_payload_printable)
    print(nids_log_file_path)
    print(nids_timestamp)
    '''
    return [("nids_action",nids_action),("nids_category",nids_category),\
           ("nids_signature",nids_signature),("nids_dest_host",nids_dest_host),\
           ("nids_dest_ip",nids_dest_ip),("nids_dest_port",nids_dest_port),\
           ("nids_dest_project",nids_dest_project),("nids_dest_service",nids_dest_service),\
           ("nids_dest_user",nids_dest_user),("nids_src_host",nids_src_host),\
           ("nids_src_ip",nids_src_ip),("nids_src_port",nids_src_port),\
           ("nids_src_project",nids_src_project),("nids_src_service",nids_src_service),\
           ("nids_src_user",nids_src_user),("nids_payload",nids_payload),\
           ("nids_payload_printable",nids_payload_printable),("nids_log_file_path",nids_log_file_path),\
           ("nids_timestamp",nids_timestamp)]

def extract(nhids_result):
    final_events = []
    for each_tuple in nhids_result:
        hids = each_tuple[0]
        nids = each_tuple[1]
        each_result = dict(_hids_extract(hids) + _nids_extract(nids))
        #print(each_result,type(each_result))
        final_events.append(json.dumps(each_result))
    return final_events
