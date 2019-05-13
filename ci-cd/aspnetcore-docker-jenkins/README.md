# Docker Series
https://code-maze.com/docker-series/

## Part 1 of the Docker Series on CodeMaze blog
https://code-maze.com/how-to-prepare-aspnetcore-app-dockerization/


### build the code
> docker run --rm -it -w /home/app/AccountOwnerServer/ -v ${PWD}:/home/app microsoft/dotnet:2-sdk dotnet build

### run the code
> docker run --rm -it -w /home/app/AccountOwnerServer/ -p 8080:5000 -v ${PWD}:/home/app microsoft/dotnet:2-sdk dotnet run

### go to swagger
http://localhost:8080/swagger/

Navigate to /AccountOwnerServer and then type dotnet publish. This will publish the application into the ./bin/Debug/netcoreapp2.0/publish directory.

Now verify the dockerfile

> docker build -t jitendersharma/accountapp .

> docker run -p 8080:80 jitendersharma/accountapp



