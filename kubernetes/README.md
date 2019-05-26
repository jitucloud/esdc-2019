## Kubernetes

### Install on mac
> brew install kubectl

> brew cask install minikube

### install xhyve driver and execute permissions

> brew install docker-machine-driver-xhyve

### To start the minikube cluster
> minikube start --vm-driver:xhyve

### to see the dashboard
> minikube dashboard

### To stop the cluster
> minikube stop

### To completely delete the cluster
> minikube delete

#### https://kubernetes.io/docs/tutorials/hello-minikube/

### After pods and service are created , run the below to see the service from outside
> kubectl get services
> minikube service {service-name}
> minikube service hello-node

#### Type can be "ClusterIP", "ExternalName", "LoadBalancer", "NodePort"
### Expose pods as service
> kubectl expose pod esdc --type=NodePort --port=8080

### Expose replication controller as service
> kubectl expose rc esdc --type=NodePort --port=8080

### Expose deployment as service
> kubectl expose deployment esdc --type=NodePort --port=8080

### If you don't want to run expose command seperately, create another YML file and run that after pods are created

### kubectl commands

#### create pods using YML file
> kubectl create -f pod.yml 

#### get nodes
> kubectl get nodes

#### get pods
> kubectl get pods

#### describe pod
> kubectl describe pod {name}

#### get all the pod IP's
> kubectl get ep    
