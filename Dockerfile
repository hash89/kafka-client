FROM centos:7
MAINTAINER Hadrien PUISSANT <hpuissant@cyres.fr> && Erwann CLOAREC <ecloarec@cyres.fr>

WORKDIR /opt
RUN yum update -y && yum install -y wget python git

# Retreive JDK
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.rpm
RUN rpm -ivh jdk-8u91-linux-x64.rpm \
  && rm jdk-8u91-linux-x64.rpm

# Retreive python pip and install requests module
RUN wget https://bootstrap.pypa.io/get-pip.py \
	&& python get-pip.py \
	&& pip install requests

# Retreive kafka files
ADD http://apache.trisect.eu/kafka/0.10.0.0/kafka_2.11-0.10.0.0.tgz .
RUN tar xzf kafka_2.11-0.10.0.0.tgz && mv kafka_2.11-0.10.0.0 kafka

WORKDIR kafka/

# Retreive Kafka client file
ADD src/ kafka-client/
RUN chmod u+x kafka-client/kafka-client

WORKDIR kafka-client/

