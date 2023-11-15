# Overview
Minikube is a companion project maintained by Kubernetes authors to create an kubernetes cluster running on a single machine to test. 
It is compatible with docker containers and it enables the ability to deploy various docker containers into Kubernetes cluster.

# installation

Refer to https://minikube.sigs.k8s.io/docs/start/

> `curl -LO https://storage.googleapis.com/minikube/releases/latest/ minikube-linux-amd64`

> `sudo install minikube-linux-amd64 /usr/local/bin/minikube`

# Helpful commands
* To start Kubernetes cluster locally on a machine

> `minikube start`

To check active clusters, open a dashboard

> `minikube dashboard
`