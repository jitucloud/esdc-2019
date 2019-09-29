insert into outbox values (gen_random_uuid(),'order','123','ordercreated','{"title": "Sleeping Beauties", "genres": ["Fiction", "Thriller", "Horror"], "published": false}')



docker run --tty \
           --network kafka_bridge \
           confluentinc/cp-kafkacat:5.3.1 \
           kafkacat -b broker1:29092 -C -K: \
                    -f '\nKey (%K bytes): %k\t\nValue (%S bytes): %s\n\Partition: %p\tOffset: %o\n--\n' \
                    -t outbox.event.order
