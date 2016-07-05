import requests
import sys
import os
import os.path
import json
from print_function import *
from common import get_first_broker
# Exemple
# main.py connect startprocess /opt/kafka/conf/connect-distributed.propertie
# main.py connect list
# main.py connect plugin
# main.py connect get connector1
# main.py connect create connector1.json
# main.py connect status connector1
# main.py connect pause connector1
# main.py connect resume connector1
# main.py connect restart connector1
# main.py connect delete conncector1
# main.py connect tasks connector1
# main.py connect tasks status task1
# main.py connect tasks restart task1
# main.py connect config connector1
# main.py connect config connector1 alter connector1.json

KAFKA_HOME = str(os.getenv("KAFKA_HOME"))
KAFKA_BROKERS = str(os.getenv("KAFKA_BROKERS"))
KAFKA_ZOOKEEPER = str(os.getenv("KAFKA_ZOOKEEPER"))
KAFKA_CONNECT = str(os.getenv("KAFKA_BROKERS")) if not os.getenv("KAFKA_CONNECT") else str(os.getenv("KAFKA_CONNECT"))

def connect(argv):
    argv_len = len(argv)
    if argv_len == 3 and argv[2] in ["startprocess","list","plugin"]:
        globals()[argv[2]]()
    elif argv_len == 4 and argv[2] in ["startprocess","get","status", "pause","resume","restart","delete","create"]:
        globals()[argv[2]](argv[3])
    elif argv_len >= 5 and argv_len <=6 and argv[3] ==  "tasks":
        if argv_len == 5:
            tasks(connector_name=argv[2])
        elif argv_len == 6:
            tasks(connector_name=argv[2], task_id=argv[5], action=argv[4])
        else:
            connect_tasks_usage()
    elif argv_len >= 4 and argv_len <= 6 and argv[2] ==  "config":
        if argv_len == 4:
            config(connector_name=argv[3])
        elif argv_len == 6:
            config(connector_name=argv[3], conf_file_name=argv[4])
        else:
            connect_config_usage()
    else:
        connect_usage()

def startprocess(config_file_path=None):
    DEFAULT_CONF = KAFKA_HOME+"config/connect-distributed.properties"
    CONNECT_SCRIPT = KAFKA_HOME+"bin/connect-distributed.sh "
    BACKGROUND = " > connect-distributed.log 2>&1 &"

    if config_file_path:
        if os.path.exists(config_file_path):
            os.system(CONNECT_SCRIPT+config_file_path+BACKGROUND)
        else:
            print config_file_path+" not found."
    elif not config_file_path:
        if os.path.exists(DEFAULT_CONF):
            warning_not_found("Config file path given","Using default one : "+DEFAULT_CONF)
            os.system(CONNECT_SCRIPT+DEFAULT_CONF+BACKGROUND)
        else:
            error_not_found("Default config file",DEFAULT_CONF)



def restart(connector_name):
    print "WARNING : restarting a connector should restart the connector itself and its tasks. BUT it actually doesn't"
    resp = requests.post("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/restart")
    print 'POST /connectors/'+connector_name+'/restart {}'.format(resp.status_code)

def pause(connector_name):
    resp = requests.put("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/pause")
    print 'PUT /connectors/'+connector_name+'/pause {}'.format(resp.status_code)


def delete(connector_name):
    resp = requests.delete("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name)
    print 'DELETE /connectors/'+connector_name+' {}'.format(resp.status_code)

def plugin():
    print "not defined yet"

def resume(connector_name):
    resp = requests.put("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/resume")
    print 'PUT /connectors/'+connector_name+'/resume {}'.format(resp.status_code)

def list():
    resp = requests.get("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors")
    if resp.status_code == 200 and len(resp.json()) != 0:
        print "Existing connectors :"
        for todo_item in resp.json():
            print "  - "+todo_item
    elif resp.status_code == 200 and len(resp.json()) == 0:
        print "No connector (yet ?)"
    else:
        error_http_resp(resp)

def create(json_file_name):
    if os.path.exists(json_file_name):
        connector_properties = json.loads(open(json_file_name).read())
        resp = requests.post("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors", json=connector_properties)
        if resp.status_code == 201 and len(resp.json()) != 0:
            connector = resp.json()
            print "Connector name : "+str(connector['name'])
            print "  State : "+connector['connector']['state']
            for c in connector['tasks']:
                print "  Task %s is %s on %s" % (c['id'],c["state"], c['worker_id'])
        else:
            error_http_resp(resp)
    else:
        error_not_found("File",json_file_name)

def get(connector_name):
    resp = requests.get("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name)
    if resp.status_code == 200 and len(resp.json()) != 0:
        name = resp.json()['name']
        tasks = resp.json()['tasks']
        config = resp.json()['config']
        print "\nConnector name : "+name+"\n"
        print "Tasks list"
        for t in tasks:
            print " - Task "+str(t['task'])
        print "\nConnector configuration"
        for c in config:
            print "%15s :  %s" % (c, config[c])
        print "\n"
    else:
        error_http_resp(resp)

def status(connector_name):
    resp = requests.get("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/status")
    if resp.status_code != 200:
        print "Error "+str(resp.status_code)+" "+resp.json()['message']
        print "(with the request : http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/status)"
    elif resp.status_code == 200 and len(resp.json()) != 0:
        connector = resp.json()
        print "Connector name : "+str(connector['name'])
        print "  State : "+connector['connector']['state']
        for c in connector['tasks']:
            print "  Task %s is %s on %s" % (c['id'],c["state"], c['worker_id'])

def config(connector_name, conf_file_name=None):
    if connector_name and not conf_file_name:
        get_config(connector_name)
    elif connector_name and conf_file_name:
        update_config(connector_name, conf_file_name)

def get_config(connector_name):
    print "Not imlemented yet"

def update_config(connector_name, conf_file_name=None):
    print "Not imlemented yet"

def tasks(connector_name, task_id=None, action=None):
    if connector_name and not task_id and not action:
        tasks_list(connector_name)
    elif connector_name and task_id and action:
        globals()["tasks_"+action](connector_name=connector_name, task_id=task_id)

def tasks_list(connector_name):
    resp = requests.get("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/tasks")
    if resp.status_code != 200:
        print "Error "+str(resp.status_code)+" "+resp.json()['message']
        print "(with the request : http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/tasks)"
    elif resp.status_code == 200 and len(resp.json()) != 0:
        for todo_item in resp.json():
            print "Task id : "+str(todo_item["id"]['task'])
            print "  Connector : "+todo_item["id"]['connector']
            print "  Configuration"
            for c in todo_item["config"]:
                print "  %10s : %s" % (str(c), todo_item["config"][c])

def tasks_status(connector_name, task_id):
    resp = requests.get("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/tasks/"+task_id+"/status")
    if resp.status_code != 200:
        print "Error "+str(resp.status_code)+" "+resp.json()['message']
        print "(with the request : http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/tasks/"+task_id+"/status)"
    elif resp.status_code == 200 and len(resp.json()) != 0:
        print "Task "+task_id
        for todo_item in resp.json():
            print "  %10s : %s" % (todo_item, resp.json()[todo_item])

def tasks_restart(connector_name, task_id):
    resp = requests.post("http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/tasks/"+task_id+"/restart")
    if resp.status_code != 204:
        print "Error "+str(resp.status_code)
        print "(with the request : http://"+get_first_broker(KAFKA_CONNECT)+":8083/connectors/"+connector_name+"/tasks/"+task_id+"/status)"
