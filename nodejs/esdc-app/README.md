## simple node js hello world app
## simple dockerfile

### create docker swarm service with version

> docker service create --name esdc-hw --network ps-net -p 8080:8080 --replicas 12 jitendersharma/esdc-hw:v1

### go to manager
> docker service inspect --pretty esdc-hw

### docker service rolling update
> docker service update --image jitendersharma/esdc-hw:v2 --update-parallelism 2 \
> --update-delay 10s esdc-hw 

###  check that config is updated
> docker service inspect --pretty esdc-hw
