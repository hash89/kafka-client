import os
from print_function import console_usage

KAFKA_HOME = str(os.getenv("KAFKA_HOME"))
ZOOKEEPER = "localhost:2181"
BROKER_LIST = "localhost:9092"

def console(argv):
    if len(argv) == 4 and argv[2] == "consume":
        consume(topic_name=argv[3])
    elif len(argv) == 5 and argv[2] == "consume" and argv[4] == "beginning":
        consume(topic_name=argv[3], from_beginning=True)
    elif len(argv) == 4 and argv[2] == "produce":
        produce(topic_name=argv[3])
    else:
        console_usage()

def consume(topic_name, from_beginning=False):
    if not from_beginning:
        os.system(KAFKA_HOME+"bin/kafka-console-consumer.sh --zookeeper "+ZOOKEEPER+" --topic "+topic_name)
    else:
        os.system(KAFKA_HOME+"bin/kafka-console-consumer.sh --zookeeper "+ZOOKEEPER+" --topic "+topic_name+" --from-beginning")

def produce(topic_name):
    os.system(KAFKA_HOME+"bin/kafka-console-producer.sh --broker-list "+BROKER_LIST+" --topic "+topic_name)
