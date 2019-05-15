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
### run unit test locally
> python3 test-local.py   

## Run in selenium grid
### Chrome
> export BROWSER=chrome && python3 test.py
### Firefox
> export BROWSER=firefox && python3 test.py

### To simulate a longer test run, let's run the same test sequentially twenty times—ten on Chrome, ten on Firefox.
### run test in sequence
> python3 sequential_test_run.py

### Run paralle
> python3 parallel_test_run.py

### kill all docker containers 
> docker rm $(docker ps -a -q) -f


