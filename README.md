## Environment

This app was developed in PyCharm Professional running on Windows 10 Pro.  
Therefore, I will list requirements, testing method, and installation on this system.

### System Requirements

Enable Hyper-V
 - dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
 - bcdedit /set hypervisorlaunchtype auto  

Enable SVM in BIOS. (System dependent)

### Software Requirements Installation

- [Docker - Docker Desktop](https://www.docker.com/products/docker-desktop/)


- [Kubernetes - Minikube](https://minikube.sigs.k8s.io/docs/start/)


- [Helm](https://helm.sh/)


- [PostgreSQL](https://www.postgresql.org/)

### App installation

From the fastapimeals/charts directory:
- helm install myapp fastapimeals-helm --namespace fastapimeals-namespace --create-namespace

Wait a little, till it installs, then:
- minikube service nginx-service-myapp-fastapimeals-helm --url -n fastapimeals-namespace

Keep this terminal open.  
This port forwarding is needed because using Docker Desktop with Minikube.  
You will get an URL similar to: http://127.0.0.1:50783  
You can reach the application at URL/docs, in this case: http://127.0.0.1:50783/docs

### App uninstallation

 - helm uninstall myapp --namespace fastapimeals-namespace

## Developer Environment

Make sure to update the environment variables in **mealsapp/config.py**, before starting up the project.  
You need to create the databases before you can connect.  
Make sure to install software requirements above, and I suggest using PyCharm Professional:
- PyCharm Professional (https://www.jetbrains.com/pycharm/)

I used helm, to install a postgres db on the minikube:
- helm repo add bitnami https://charts.bitnami.com/bitnami
- helm repo update
- helm install postgres-local --set auth.postgresPassword=test bitnami/postgresql --namespace mealsapp-local --create-namespace
- kubectl port-forward --namespace mealsapp-local postgres-local-postgresql-0 5432:5432 (in a separate shell, keep this running)
- psql --host 127.0.0.1 -U postgres -d postgres -p 5432
- create database mealsappdb;
- create database testdb;
- exit;

#### Python Dependencies

Install Python Packages from the python environment you use:
 - pip install -r requirements.txt

After this, you can run the app from PyCharm, and can reach the app on http://127.0.0.1:8000/docs  
You can run all unittests by choosing Run -> Run... -> Pytest  
Or individually by clicking the green arrow next to the methods in the tests package.

## Updating Docker Image

After local testing, rebuild docker image:
 - docker build -t andrewhorvath8/fastapimeals .  

And push to hub (after docker login):
 - docker push andrewhorvath8/fastapimeals

## GitHub
 - [https://github.com/andrewhorvath8/fastapi_mealsapp](https://github.com/andrewhorvath8/fastapi_mealsapp)

## DockerHub
 - [https://hub.docker.com/repository/docker/andrewhorvath8/fastapimeals](https://hub.docker.com/repository/docker/andrewhorvath8/fastapimeals)


## References

Major references used for this app:

 - First and foremost, the FastAPI guide hosted on jetbrains made by Mukul Mantosh. (https://www.jetbrains.com/pycharm/guide/tutorials/fastapi-aws-kubernetes/)
 - FastAPI documentation. (https://fastapi.tiangolo.com/)
 - SQLAlchemy documentation. (https://www.sqlalchemy.org/)
 - Kubernetes documentation. (https://kubernetes.io/docs/home/)
 - Helm documentation. (https://helm.sh/)
 - Google :)