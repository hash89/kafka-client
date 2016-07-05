import os
from print_function import console_usage

KAFKA_HOME = str(os.getenv("KAFKA_HOME"))
KAFKA_BROKERS = str(os.getenv("KAFKA_BROKERS"))
KAFKA_ZOOKEEPER = str(os.getenv("KAFKA_ZOOKEEPER"))
KAFKA_CONNECT = str(os.getenv("KAFKA_BROKERS")) if not os.getenv("KAFKA_CONNECT") else str(os.getenv("KAFKA_CONNECT"))

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
        os.system(KAFKA_HOME+"bin/kafka-console-consumer.sh --zookeeper "+KAFKA_ZOOKEEPER+" --topic "+topic_name)
    else:
        os.system(KAFKA_HOME+"bin/kafka-console-consumer.sh --zookeeper "+KAFKA_ZOOKEEPER+" --topic "+topic_name+" --from-beginning")

def produce(topic_name):
    os.system(KAFKA_HOME+"bin/kafka-console-producer.sh --broker-list "+KAFKA_BROKERS+" --topic "+topic_name)
