import os
import sys
from print_function import *

KAFKA_HOME = str(os.getenv("KAFKA_HOME"))
KAFKA_BROKERS = str(os.getenv("KAFKA_BROKERS"))
KAFKA_ZOOKEEPER = str(os.getenv("KAFKA_ZOOKEEPER"))
KAFKA_CONNECT = str(os.getenv("KAFKA_BROKERS")) if not os.getenv("KAFKA_CONNECT") else str(os.getenv("KAFKA_CONNECT"))
KAFKA_COMMAND = KAFKA_HOME+'bin/kafka-topics.sh --zookeeper '+KAFKA_ZOOKEEPER
KAFKA_COMMAND += ' --topic '+sys.argv[3] if len(sys.argv) >= 4 else ""

def topic(argv):
    if len(argv) > 2:
        if argv[2] == "create" and len(argv) >= 6:
            config = argv[6] if len(argv) == 7 else None
            create(partition=argv[4], replication=argv[5], config=config)
        elif argv[2] in ["describe","delete","list"]:
            action(action=argv[2])
        elif argv[2] == "config" and len(argv) == 6:
            configure(argv=argv)
        else:
            topic_usage()
    else:
        topic_usage()

def create(partition=None, replication=None, config=None):
    command = KAFKA_COMMAND+' --create --replication-factor '+replication+' --partitions '+partition
    command += ' --config '+config if config else ""
    os.system(command)

def action(action):
    os.system(KAFKA_COMMAND+" --"+action)

def configure(argv):
    if argv[4] == "alter" and len(argv) == 6:
        os.system(KAFKA_COMMAND+' --alter --config '+argv[5])
    elif argv[4] == "delete" and len(argv) == 6:
        os.system(KAFKA_COMMAND+' --alter --delete-config '+argv[5])
    else:
        topic_usage()
