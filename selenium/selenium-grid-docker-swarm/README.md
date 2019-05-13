# Run selenium grid using docker-swarm on play with docker

## create a docker swarm cluster with one manager and more then one worker

## Create a new session on play with docker. You can get upto 4 session here
https://labs.play-with-docker.com


## How to get hit the deployed app
https://github.com/play-with-docker/play-with-docker

### example
> http://ip172-18-0-32-bjcjpv7dqii000dvr3q0-4444.direct.labs.play-with-docker.com


### go to the main folder
> docker stack deploy -c docker-compose.yml selenium

### list the service
> docker service ls

### scale the browser
> docker service scale chrome=5

### check the docker swarm manager/worker
> docker node ls     (run this on manager)

