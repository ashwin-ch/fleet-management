# Fleet-management application

## Assignment details
* *Topic: Build something*
* *Developer: Ashwin Kumar Ganesan*
* _email: asga23@student.bth.se_

# Link to project
Below repository contains the project along with deployment yaml manifests.

[github:fleet-management-repo](https://github.com/ashwin-ch/fleet-management/tree/main)



# Project overview
Fleet management system for machinery vehicles enables operation and maintenance of vehicles deployed in a site.
The vehicle contain a on-board fleet agent, which provides various insights from the vehicle. Provides ability to control, manage and diagnose
vehicle features and faults.
This system also schedules assignment and tracks payload of the vehicle, and its efficiency.

Provides insight on,
- Vehicle identity
- Vehicle accessories
- Vehicle active status
- Interaction between vehicle and offboard agent

Possible expansion for
- Fleet statistics
- Driver productivity
- Site statistics
- Fuel statistics
- Map updates


# Design overview
![Deployment architecture](image_v2.png)


# Technical specification
The solution is developed based on microservices executing on docker images, there are two microservices running, i.e. fleet-application and vehicle-off-board-manager, along with a fleet-server.

The purpose of fleet-application is to provide interface for site-operators to find the list of vehicles and their statistics on a web-ui. While the vehicle-off-board-manager provides ability for vehicle to connect with the server to push and pull data. This manager has the ability to push goals and target site activities like loading, dumping etc. while also allows vehicle to push notification on service required, driver details, vehicle status. There is a simple node json.server deployed in the background, which is a centralized between both the applications to fetch and update information spontaneously.

## Fleet server
This is a simple vehicle database constructed for this concept based on json-server, which contains different parameters
relevant to the vehicle for providing insights to supervisor through front-end dashboard

## Fleet Application
Fleet application component is developed based on javascript, css and html, to be able to process the information from database and
provide a dashboard view through a web-client for site supervisors. This has possible extension to diagnose individual vehicle, assign tasks
to different machineries.

## Vehicle offboard agent (vehicle manager)
Vehicle manager is a microservice deployed in order to bridge between the off-board and on-board systems. This agent is developed using Flask-python.
This provides REST Calls for vehicle to connect, get information about the vehicle assignment, map data and upload vehicle diagnostics data, fuel statistics, payload statistics and assignment status for autonomous control vehicles. For this prototype, we use CURL commands to connect to the vehicle-agent as experiement, while the on-board device on machine can use RestAPIs to communicate with vehicle-off-board-agent.


# Docker images

## Fleet server
[aganesa2/fleetserver:dev](https://hub.docker.com/repository/docker/aganesa2/fleetserver/general)

## Fleet manager
[aganesa2/fleetserver:dev](https://hub.docker.com/repository/docker/aganesa2/fleetmgr/general)

## Vehicle manager
[aganesa2/vehiclemgr:dev](https://hub.docker.com/repository/docker/aganesa2/vehiclemgr/general)


## Start minikube and ensure pods are running
Start minikube
> $ minikube start

Check running nodes with minikube a part of it
> $ kubectl get nodes

Start a k8 dashboard in a separate terminal
> $ minikube dashboard
_if necessary some addons might be required to be enabled before starting a dashboard_
This opens a dashboard in [127.0.0.1:39507](http://127.0.0.1:39507/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/workloads?namespace=default)

## Starting applications using K8s in minikube
To create a pod using locally built image
> $ kubectl apply -f fleet-deployment-v1.yaml

To create services required for deployment
> $ minikube service fleet-service
> $ minikube service fleet-manager-service

To check if the pods are running
> $ kubectl get pods
> $ kubectl get services

To delete a deployment created in K8s
> $ kubectl delete -n default deployment fleet-deployment

The dashboard should be able to provide insights on the deployment, pods, services and logs.

# Questions & discussion: 
## Benefits and challenges behind the architecture pattern being used?
Microservice architecture is well-known for large application software developed in different environments and toolchains, 
while integrated provides an enterprise solution or a large-scale application. This model or architecture provides the flexibility to develop smaller, stateless applications that can function independently and have the ability to be deployed and scaled on a larger scale. 
In particular, we have utilized the decomposition type of the coarse gain model, which provides the encapsulation of broader capabilities in terms of business and the ability to have many smaller components internally. 
The communication incorporated is asynchronous to have the ability to provide events and message queue mechanisms for communication. This allows services to operatindependently.
This design or architecture enables cross-functional teams to choose toolchain, and build systems and programming methods based on the criteria. 
In our use case a web-cline application can be developed in node.js, while the vehicle agents can be developed in FlaskPy, an extension based on Python. 
This enables the on-board team developing embedded applications to also develop a service that can be deployed on cloud and also maintain the interfaces between the fleet(vehicles) and the server(domain). 

## Challenges encountered during design and development of the application
- Creating a network composition and configuring the cluster, nodes and pods with regards to the configuration has been a hazzel in the beginning
- Choosing the right type of database skeleton 

## How to mitigate the challenges
- Creating a network architecture for the project based on requirements and scope would help us identify the list of techniques and services we need to incorporate to achieve a better deployment model. 
- Finding the right form of database which is suitable for project scope, lifetime and use-case would help us achieve scalability of the application
- Also drafting and designing the intended network policies based on the project requirements is required to have stable and secure deployment model. 
- Have a logical architecture sketch in order to identify the logical elements present in the project. And decompose the logical elements into system/software elements and configurations. 

## Security aspects in current design
We haven't incorporated any security mechanism in the current design, but based on the knowledge and understanding, security has to be incorporated in different level within cloud infrastructure, i.e, underlaying infrastructure, Kubernetes level and application level, since attack can happen at any level. 

Basic level of security can be achieve by creating the image from secure sources so the image is stable and secure without unauthorized traces or doesn't contains untrusted registries. 
Run applciations with appropriate user access in-order to avoid unintended access rights and ability to perform vulnurable tasks. Creating necessary user-groups and corresponding permissions will enhance the execution and regulate the access to Kubernetes. Also having role based access configuration helps to better streamline and protection towards the data or application. 

Another main aspect of security is, `etcd` every metadata or information regards to the cluster is maintained here. And it is very important to protect or secure this. `etcd` can be maintained inside or outside the cluster. While having inside the cluster, we can introduce a firewall to protect the `etdc`. Also by encrypting the `etcd`, the data can be protected from unintentded attack. And finally the application and its interfaces and APIs needs to be secured, eg. Ingress controller which can provide Security over http and other techniques like SSL and TSL. 

Also it is required to have a backup and recovery mechanism incorporated as part of the CI/CD pipelies would be benefial and value. 
