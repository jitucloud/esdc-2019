# how to run selenium grid on docker using docker-compose

# install docker on host machine
# go to the folder
# run
> docker-compose up  -d

# navigate to the selenium grid
> hit http://{hostname}:4444

# stop
> docker-compose down

# scale
> docker-compose scale chrome=5

### go to testcase folder
### make sure you have python3 and selenium webdriver installed
### run unit test
> python3 test.py


