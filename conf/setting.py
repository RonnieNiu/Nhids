# set nids and hids intervel time
INTERVAL = "15"

#set log path
LOGPATH = "/opt/Nhids/log/"

#set es host and auth password
ES_HOST = ["http://10.212.18.29:9200","http://10.212.21.60:9200"]
ES_AUTH = ("elastic","abc123!@#")

#set redis host and auth password
REDIS_HOST = "10.212.18.29"
REDIS_PORT = 6390
REDIS_AUTH = "abc123!@#"
REDIS_DB = 0

#set final_events index in elastic
NHIDS_INDEX = "nhids_event"
