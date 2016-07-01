import os
from print_function import consumergroup_usage

# Exemple
# main.py consumergroup list
# main.py consumergroup describe groupe1
KAFKA_HOME = str(os.getenv("KAFKA_HOME"))
ZOOKEEPER = "localhost:2181"
KAFKA_COMMAND = KAFKA_HOME+"bin/kafka-consumer-groups.sh --zookeeper "+ZOOKEEPER

def consumergroup(argv):
    if len(argv) == 3 and argv[2] == "list":
        list()
    elif len(argv) == 4 and argv[2] == "describe":
        describe(argv[3])
    else:
        consumergroup_usage()

def list():
    os.system(KAFKA_COMMAND+" --list")

def describe(consumergroup_name):
    os.system(KAFKA_COMMAND+" --describe --group "+consumergroup_name)
