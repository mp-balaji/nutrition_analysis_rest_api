# Kubernetes

The application is deployed to Kubernetes using the code in this directory. This README contains a basic description of what each of these files is for and how they are used to deploy the application to the cloud.

## Deployment

 The main manifest that defines how the application is deployed to the Kubernetes cluster is the `deployment.yaml` file. A key feature of this file is the `spec` (specification) section that defines the containers that are running on the pods, that are deployed when this file is applied in the cluster. A Kubernetes pod is the most fundamental deployable unit in Kubernetes and represents a single instance of a running process in the cluster. In this case the specification section for the pods defines two containers (which can communicate over localhost as they are running on the same machine) and a volume to store some secrets needed to connect to the database when running in the cloud.

 The main container running on the pods deployed using this manifest is the application container. This is running the application docker image. This is currently pulled from a docker hub repository. Anyone can create a docker image and push this to their own public dockerhub account if they wish to update this image value. The application port is defined in this file, and there are a number of environment variables also defined that allow the app to connect to the database. Some of these are again being read from a Kubernetes secret that has been manually created in the GCP project used to deploy the Kubernetes cluster and database. Memory and CPU resources are also defined for this container for reasons that will be explained in a later section of this README. The other container defined is running an image pulled from a GCP google container registry. This container runs a cloud proxy that enables the application to read securely from the Cloud SQL database instance deployed in GCP. This additional container is referred to as a sidecar. More information about how communication with the database works and how it is deployed can be found in the main application README.

 Other things defined in this file are the number of desired replicas. This means that multiple pods can be deployed, ensuring that traffic can be load balanced across multiple instances of the application.

 ## Service

 The `service.yaml` defines a LoadBalancer that is deployed to the Kubernetes cluster. This is directed to send traffic to the deployment using the `selector` key, which has a value of `nutrition-analysis-app`, i.e. the name of the deployment. If the number of pods deployed changes then the service will automatically start or stop sending traffic to the pods that are added/removed. The LoadBalancer when deployed will expose a public IP address that can be used to access the application in a browser alongside the port that is defined in this file.

 ## Horizontal Pod Autoscaler (HPA)

 Another resource that can be deployed from these files is an HPA that allows the cluster to automatically deploy new application pods based on the resource utilisation defined in `hpa.yaml`. The minimum and maximum replicas is defined in this file, as well as the thresholds that have to be reached in order to trigger the deployment of a new replica (pod). The resources provided to the app containers (as mentioned in the deployment section of this README) are set to low values, and the HPA threshold is also set to a low value to ensure this functionality can be demonstrated easily.

 ## Service Account

The `service-account.yaml` file is used to assign a GCP service account to the cluster in order to grant access to the Cloud SQL database instance in GCP. Without this the application would not be able to access the database via the cloud sql proxy. More information on how this was created and how the cluster was configured can be found in the main README.