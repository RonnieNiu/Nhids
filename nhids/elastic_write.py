#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elastic_conn import es
from elasticsearch import helpers

from log import log_decorator
from conf import setting

@log_decorator
def _create_index():
    #jundge index is exist in elastic or not,if not,create it 
    if es.indices.exists(index=setting.NHIDS_INDEX) != True:
        body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1},
                #            "hids_agent_ip":{"type": "text"},
                #            "hids_srcip":{"type": "text"},
                #            "hids_srcport":{"type": "text"},
                #            "hids_node":{"type": "text"},
                #            "hids_rule_description":{"type": "text"},
                #            "hids_rule_level":{"type": "text"},
                #            "hids_full_log":{"type": "text"},
                #            "hids_timestamp":{"type": "date"},
                #            "nids_action":{"type": "text"},
                #            "nids_category":{"type": "text"},
                #            "nids_signature":{"type": "text"},
                #            "nids_dest_host":{"type": "text"},
                #            "nids_dest_ip":{"type": "text"},
                #            "nids_dest_port":{"type": "text"},
                #            "nids_dest_project":{"type": "text"},
                #            "nids_dest_service":{"type": "text"},
                #            "nids_dest_user":{"type": "text"},
                #            "nids_src_host":{"type": "text"},
                #            "nids_src_ip":{"type": "text"},
                #            "nids_src_port":{"type": "text"},
                #            "nids_src_project":{"type": "text"},
                #            "nids_src_service":{"type": "text"},
                #            "nids_src_user":{"type": "text"},
                #            "nids_payload":{"type": "text"},
                #            "nids_payload_printable":{"type": "text"},
                #            "log_file_path":{"type": "text"},
                #            "nids_timestamp":{"type": "date"}
                #            }
                #}
        }
        try:
            res = es.indices.create(index=setting.NHIDS_INDEX,body=body,ignore=400)
            return None
        except Exception as e:
            return e

@log_decorator
def WriteInputElastic(final_events):
    _create_index()
    try:
        res = helpers.bulk(es,actions=final_events,index=setting.NHIDS_INDEX,doc_type="nhids")
        return res[0]
    except Exception as e:
        return e
