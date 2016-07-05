import os
import os.path
from print_function import *

# Exemple
# main.py zookeeper start
# main.py zookeeper start /home/user/kafka/config/zookeeper.propersties
# main.py zookeeper stop
# main.py zookeeper restart
# main.py zookeeper restart /home/user/kafka/config/zookeeper.propersties

KAFKA_HOME = str(os.getenv("KAFKA_HOME"))
LOG_DIR = "zookeeper.log"
BACKGROUND = " > "+LOG_DIR+" 2>&1 &"
DEFAULT_CONF = KAFKA_HOME+"config/zookeeper.properties"

def zookeeper(argv):
    argv_len = len(argv)

    if argv_len >= 3 and argv_len <= 4 and argv[2] == "start":
        if argv_len == 3:
            zookeeper_start()
        else:
            zookeeper_start(config_file_path=argv[3])
    elif argv_len == 3 and argv[2] == "stop":
        zookeeper_stop()
    elif argv_len == 4 and argv[2] == "restart":
        if argv_len == 3:
            zookeeper_restart()
        else:
            zookeeper_restart(config_file_path=argv[3])
    else:
        zookeeper_usage()

def zookeeper_start(config_file_path=None):
    if config_file_path:
        if os.path.exists(config_file_path):
            os.system(KAFKA_HOME+"bin/zookeeper-server-start.sh "+config_file_path+BACKGROUND)
        else:
            print "Config file "+config_file_path+" not found."
    else:
        if os.path.exists(DEFAULT_CONF):
            os.system(KAFKA_HOME+"bin/zookeeper-server-start.sh "+DEFAULT_CONF+BACKGROUND)
        else:
            print "Default config file "+DEFAULT_CONF+" not found."

def zookeeper_stop():
    os.system(KAFKA_HOME+"bin/zookeeper-server-stop.sh")

def zookeeper_restart(config_file_path=None):
    zookeeper_stop()
    zookeeper_start(config_file_path=config_file_path)
