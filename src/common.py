import os
import os.path

def checkConfigFile(path):
    if not os.path.isfile(path):
        print "Config file not found"

def get_first_broker(brokers):
    return brokers.split(",")[0].split(":")[0]

def getMissingEnvVar():
    error_msg = "\nThe following env variable are not set :\n"
    if not os.getenv('KAFKA_HOME'):
        error_msg += "- KAFKA_HOME\n"
    if not os.getenv('KAFKA_BROKERS'):
        error_msg += "- KAFKA_BROKERS\n"
    if not os.getenv('KAFKA_ZOOKEEPER'):
        error_msg += "- KAFKA_ZOOKEEPER\n"
    if not os.getenv('KAFKA_CONNECT'):
        error_msg += "- KAFKA_CONNECT\n"
    return error_msg
