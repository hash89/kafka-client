# kafka-cli
Command line tool for managing kafka and kafka connect.

The goal of this cli, is to facilitate the use of kafka scripts and REST API call.

You can find all the command here : https://kafka.apache.org/documentation.html

Before starting, you will need 3 (or 4) environement variables
- KAFKA_HOME : define the kafka root to execute scripts
- KAFKA_BROKERS : used for call to kafka brokers
- KAFKA_ZOOKEEPER : used (in almost every command) for call to zookeeper
- (KAFKA_CONNECT) : used if the distributed connect process is on different hosts than kafka brokers

You can use the cli with this command, and show usage
```
$> kafka-cli
```

### Topic
Create topic with his partition number and replication factor.
Configuration arg should be x=y property type.
```
$> kafka-cli topic create topic_name topic_partition topic_replica [config]
```
Retreive information about a topic
```
$> kafka-cli topic describe topic_name
```
Delete a topic
```
$> kafka-cli topic delete topic_name
```
Get list of topic
```
$> kafka-cli topic list
```
Get the configuration of a topic
```
$> kafka-cli topic config topic_name
```
Edit the property _foo_ with the value _bar_ for the topic topic_name
```
$> kafka-cli topic config topic_name alter foo=bar
```
Delete the property _foo_ for the topic topic_name
```
$> kafka-cli topic config topic_name delete foo
```
### Connect
**Available only in distributed mode**
#### Connector lifecycle
Get the list of connectors available
```
$> kafka-cli connect list
```
Create a connector with a given json configuration file
```
$> kafka-cli connect create connect_json_file_path
```
Here is the configuration file for a source file connector :
```json
{
  "name":"apache-log-connector",
  "config":{
    "connector.class":"org.apache.kafka.connect.file.FileStreamSourceConnector",
    "file":"/var/log/apache/apache.log",
    "tasks.max":"3",
    "topic":"apache-log"        
  }
}
```
If you want more informations about the differents property, good luck ! Connectors configurations can be found in the java class on internet...

Pause, resume, restart or delete a connector
```
$> kafka-cli connect pause connector_name
$> kafka-cli connect resume connector_name
$> kafka-cli connect restart connector_name
$> kafka-cli connect delete connector_name
```
Get a connector
```
$> kafka-cli connect get connector_name
```
Get the status of a connector
```
$> kafka-cli connect status connector_name
```
#### Connector configuration
Get the configuration of a connector
```
$> kafka-cli connect config connector_name
```
Edit the configuration of a connector, with the json file given
```
$> kafka-cli connect config connector_name alter json_file_path
```
#### Connector tasks
Get the tasks of a connector
```
$> kafka-cli connect connector_name tasks list
```
Get the status of a particular task
```
$> kafka-cli connect connector_name tasks status task_id
```
Restart the task of a connector
```
$> kafka-cli connect connector_name tasks restart task_id
```
### Console
You can use those commands to use the kafka-console-producer and kafka-console-consumer scripts
```
$> kafka-cli console consume topic_name
$> kafka-cli console produce topic_name
```
### Consumer group
You can use those commands to use the kafka-consumer-groups script
```
$> kafka-cli consumergroup list
$> kafka-cli consumergroup describe consumergroup_name
```
