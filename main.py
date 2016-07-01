#!/usr/bin/python
import sys
from topic_function import *
from zookeeper_function import *
from print_function import *
from connect_function import *
from console_function import *
from consumergroup_function import *
from server_function import *

if (len(sys.argv) <= 1):
    usage()
elif not os.getenv('KAFKA_HOME') or not os.getenv('KAFKA_BROKERS') or not os.getenv('KAFKA_ZOOKEEPER'):
    print_no_env()
else:
    locals()[sys.argv[1]](sys.argv)
