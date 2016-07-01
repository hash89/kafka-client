import os
import os.path
from print_function import *

# Exemple
# main.py server start
# main.py server start /home/user/kafka/config/server.propersties
# main.py server stop
# main.py server restart
# main.py server restart /home/user/kafka/config/server.propersties

KAFKA_HOME = os.getenv("KAFKA_HOME")
LOG_DIR = "server.log"
BACKGROUND = " > "+LOG_DIR+" 2>&1 &"
DEFAULT_CONF = KAFKA_HOME+"config/server.properties"

def server(argv):
    argv_len = len(argv)

    if argv_len >= 3 and argv_len <= 4 and argv[2] == "start":
        if argv_len == 3:
            server_start()
        else:
            server_start(config_file_path=argv[3])
    elif argv_len == 3 and argv[2] == "stop":
        server_stop()
    elif argv_len == 4 and argv[2] == "restart":
        if argv_len == 3:
            server_restart()
        else:
            server_restart(config_file_path=argv[3])
    else:
        server_usage()

def server_start(config_file_path=None):
    if config_file_path:
        if os.path.exists(config_file_path):
            os.system(KAFKA_HOME+"bin/kafka-server-start.sh "+config_file_path+BACKGROUND)
        else:
            print "Config file "+config_file_path+" not found."
    else:
        if os.path.exists(DEFAULT_CONF):
            os.system(KAFKA_HOME+"bin/kafka-server-start.sh "+DEFAULT_CONF+BACKGROUND)
        else:
            print "Default config file "+DEFAULT_CONF+" not found."

def server_stop():
    os.system(KAFKA_HOME+"bin/kafka-server-stop.sh")

def server_restart(config_file_path=None):
    server_stop()
    server_start(config_file_path=config_file_path)
