import sys

def usage():
    print "Kakfa script usage"
    print ""
    print sys.argv[0]+" command"
    print "command :"
    print "   zookeeper"
    print "   server"
    print "   topic"
    print "   console"
    print "   consumergroup"
    print "   connect"

def print_no_env():
    print "Environement variable for kafka is not set, here is an exemple "
    print "   export KAFKA_HOME=path_to_kafka_home"
    print "   export KAFKA_BROKERS=broker-1:9092,broker-2:9092"
    print "   export KAFKA_ZOOKEEPER=zoo1:2181,zoo2:2181"
    print "   export KAFKA_CONNECT=connect1:8083,connect2:8083"

def connect_usage():
    print "Kafka Connect part"
    print "Available command : "
    print "   startprocess (start distributed connector process)"
    print "   list"
    print "   create 'json_file'"
    print "   get 'connector_name'"
    print "   config 'connector_name'"
    print "   config 'connector_name' alter 'json_file'"
    print "   status connector_name"
    print "   'connector_name' tasks list"
    print "   'connector_name' tasks status 'task_id'"
    print "   'connector_name' tasks restart 'task_id'"
    print "   pause 'connector_name'"
    print "   resume 'connector_name'"
    print "   restart 'connector_name'"
    print "   delete 'connector_name'"

def connect_config_usage():
    print "Available command : "
    print "   config 'connector_name'"
    print "   config 'connector_name' alter 'json_file'"

def connect_tasks_usage():
    print "Available command : "
    print "   'connector_name' tasks list"
    print "   'connector_name' tasks status 'task_id'"
    print "   'connector_name' tasks restart 'task_id'"

def console_usage():
    print "Kafka console part"
    print "Available command : "
    print "   consume 'topic_name'"
    print "   consume 'topic_name' [beginning]"
    print "   produce 'topic_name'"

def consumergroup_usage():
    print "Kafka consumer part"
    print "Available command : "
    print "   list"
    print "   describe 'consumergroup_name'"

def zookeeper_usage():
    print "Zookeeper part"
    print "Available command : "
    print "  start 'conf_file_path'"
    print "  stop"

def server_usage():
    print "Kafka server part"
    print "Available command : "
    print "  start 'conf_file_path'"
    print "  restart 'conf_file_path'"
    print "  stop"

def topic_usage():
    print "Kafka Topic part"
    print "Available command : "
    print "   create 'topic_name' 'nb_partition' 'replication_factor' [config]"
    print "      (config : x=y)"
    print "   describe 'topic_name'"
    print "   delete 'topic_name'"
    print "   config 'topic_name' alter 'property=value'"
    print "   config 'topic_name' delete 'property'"
    print "   list"

def error_not_found(msg, extra=""):
    print "Error : "+msg+" not found. "+extra

def warning_not_found(msg, extra=""):
    print "Warning : "+msg+" not found. "+extra

def error_no_connector(extra=""):
    print "There is not connector (yet) "+extra

def error_http_resp(resp):
    response = resp.json()
    print '/connectors/ {} {}'.format(response['error_code'], response['message'])
