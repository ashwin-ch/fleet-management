# Fleet-management application
The purpose of this application is to host a fleet management service for vehicles handled in any specific area, like mines or construction site. The application provides interface to find the list of active vehicle onsite and its productivity.


Provides insight on,
- Vehicle identity
- Vehicle accessories
- Vehicle active status
- Vehicle service required
- Vehicle mileage


Possible expansion for
- Fleet statistics
- Driver productivity
- Site statistics

# Technical specification
The solution is developed based on microservices executing on docker images, there are two microservices running, i.e. fleet-application and vehicle-off-board-manager, along with a fleet-server.

The purpose of fleet-application is to provide interface for site-operators to find the list of vehicles and their statistics on a web-ui. While the vehicle-off-board-manager provides ability for vehicle to connect with the server to push and pull data. This manager has the ability to push goals and target site activities like loading, dumping etc. while also allows vehicle to push notification on service required, driver details, vehicle status. There is a simple node json.server deployed in the background, which is a centralized between both the applications to fetch and update information spontaneously.

The fleet-application is developed based on node.js and also provides view for end users. While the vehicle-off-board-manager is developed based on flask-py interfacing and closing working with json server to update vehicle information.




# Handy Command for local debugging




## Building docker locally
### TBD

## Start minikube and ensure pods are running

Start minikube
> $ minikube start
>
>
Check running nodes with minikube a part of it
> $ kubectl get nodes
Start a k8 dashboard in a separate terminal
> $ minikube dashboard

This opens a dashboard in [127.0.0.1:39507](http://127.0.0.1:39507/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/workloads?namespace=default)

## Starting applications using K8s in minikube
To create a pod using locally built image
> $ kubectl create -f fleet-deployment.yaml

To check if the pods are running

> $ kubectl get pods

To delete a deployment created in K8s

> $ kubectl delete -n default deployment fleet-deployment


## Starting docker for server and various services

Starting a fleet-server
> $ docker run --network host -d -it fleetserver:dev

Start a fleet-application


Start a vehicle-off-board-manager

