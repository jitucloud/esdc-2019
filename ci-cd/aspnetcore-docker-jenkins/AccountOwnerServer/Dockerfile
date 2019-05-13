# FROM microsoft/aspnetcore:2.0 AS base
# WORKDIR /app
# EXPOSE 5000

# FROM microsoft/aspnetcore-build:2.0 AS build
# WORKDIR /src
# COPY ["ci-cd/aspnetcore-docker-jenkins/AccountOwnerServer/AccountOwnerServer.csproj", "ci-cd/aspnetcore-docker-jenkins/AccountOwnerServer/"]
# RUN dotnet restore "ci-cd/aspnetcore-docker-jenkins/AccountOwnerServer/AccountOwnerServer.csproj"
# COPY . .
# WORKDIR "/src/ci-cd/aspnetcore-docker-jenkins/AccountOwnerServer"
# RUN dotnet build "AccountOwnerServer.csproj" -c Release -o /app

# FROM build AS publish
# RUN dotnet publish "AccountOwnerServer.csproj" -c Release -o /app

# FROM base AS final
# WORKDIR /app
# COPY --from=publish /app .
# ENTRYPOINT ["dotnet", "AccountOwnerServer.dll"]

FROM microsoft/aspnetcore
 
WORKDIR /home/app
COPY bin/Debug/netcoreapp2.0/publish .
 
ENTRYPOINT ["dotnet", "AccountOwnerServer.dll"]
