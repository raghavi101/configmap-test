# About
This repository is a part of [GITOPSRVCE-119](https://issues.redhat.com/browse/GITOPSRVCE-119). It addresses the following question : 

````
Is it possible to create a Git repository which only contains a small number of Kubernetes resources, but those resources are very large. The goal here is to force Argo CD to download many MB of data from the repo.

Example: What if we have 1000 1MB ConfigMaps: this would be 1GB of data that Argo CD would have to download (and potentially keep in memory).
````
## Steps
1. Clone this repository 
```
git clone https://github.com/raghavi101/configmap-test.git
```
2. Aquire a cluster (minikube/oc etc), be sure that a ``metrics-server`` is configured within the kube-system namespace. If not then run the following command :
```
https://raw.githubusercontent.com/raghavi101/configmap-test/master/manifests/components.yaml
```
3. At the root of the cloned repository run the shell script 
#### NOTE :  'argocd' namespace will be recreated afresh. Running deployments will be disgarded.
 ```
 ./script.sh
```
