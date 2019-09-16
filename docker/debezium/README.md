https://medium.com/@tilakpatidar/streaming-data-from-postgresql-to-kafka-using-debezium-a14a2644906d
https://debezium.io/documentation/reference/0.10/tutorial.html#start-kafka-connect
https://support.etlworks.com/hc/en-us/articles/360020461693-Real-time-change-replication-with-Kafka-and-Debezium

### run it in interactive mode
> docker-compose -f docker-compose.yml up  

### verify kafka connect service    
> curl -H "Accept:application/json" localhost:8083/

### check how many connectors are present
> curl -H "Accept:application/json" localhost:8083/connectors/

### run the connector
> curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @customer-connector.json


### finally run the watcher 

> docker run -it --name watcher --network=kafka_bridge -e ZOOKEEPER_CONNECT='zookeeper:2181' -e KAFKA_BROKER='broker:29092' --rm  debezium/kafka:0.10 watch-topic -a -k dbserver1.customer.events





