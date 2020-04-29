#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Third-party libraries
from elasticsearch import Elasticsearch

from conf import setting

es = Elasticsearch(setting.ES_HOST,http_auth=setting.ES_AUTH,
                   sniff_on_start=True,sniff_on_connection_fail=True,sniff_timeout=5)
