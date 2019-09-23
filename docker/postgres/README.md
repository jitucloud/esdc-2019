#### https://hub.docker.com/r/debezium/postgres
### https://medium.com/@tilakpatidar/streaming-data-from-postgresql-to-kafka-using-debezium-a14a2644906d

Login into pgadmin gui as per details in yml file.
- add server connection into pgadmin
-- server : postgres
-- port : 5432
-- user : postgres
-- password : postgres

CREATE TABLE IF NOT EXISTS Kafka ( id SERIAL PRIMARY KEY,   name VARCHAR(50) );


CREATE TABLE IF NOT EXISTS outboxevent ( 
	id uuid PRIMARY KEY,  
	aggregatetype character varying(255) not null, 
	aggregateid character varying(255) not null, 
	type character varying(255) not null, 
	payload jsonb not null);


insert into outboxevent values (gen_random_uuid(),'order','123','ordercreated','{"title": "Sleeping Beauties", "genres": ["Fiction", "Thriller", "Horror"], "published": false}')



