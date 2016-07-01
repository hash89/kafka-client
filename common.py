import os
import os.path

def checkConfigFile(path):
    if not os.path.isfile(path):
        print "Config file not found"

def get_first_broker(brokers):
    return brokers.split(",")[0].split(":")[0]
