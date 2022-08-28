## Environment

This app was developed in PyCharm Professional running on Windows 10 Pro.  
Therefore, I will list requirements, testing method, and installation on this system.

### System Requirements

Enable Hyper-V

```Shell
dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
bcdedit /set hypervisorlaunchtype auto
```

Enable SVM in BIOS. (System dependent)

### Software Requirements Installation

- [Docker - Docker Desktop](https://www.docker.com/products/docker-desktop/)


- [Kubernetes - Minikube](https://minikube.sigs.k8s.io/docs/start/)


- [Helm](https://helm.sh/)


- [PostgreSQL](https://www.postgresql.org/)

### App installation

From the fastapimeals/charts directory:

```Shell
helm install myapp fastapimeals-helm --namespace fastapimeals-namespace --create-namespace
```

Wait a little, till it installs, then:

```Shell
minikube service nginx-service-myapp-fastapimeals-helm --url -n fastapimeals-namespace
```

Keep this terminal open.  
This port forwarding is needed because using Docker Desktop with Minikube.  
You will get a URL similar to: http://127.0.0.1:50783  
You can reach the application there. You can reach Swagger docs at URL/docs, where you can test features.

You can also find some sample curl calls in sample_curl_calls.txt.

### App uninstallation

```Shell
helm uninstall myapp --namespace fastapimeals-namespace
```

## Developer Environment

Make sure to update the environment variables in **mealsapp/config.py**, before starting up the project.  
You need to create the databases before you can connect.  
Make sure to install software requirements above, and I suggest using PyCharm Professional:
- PyCharm Professional (https://www.jetbrains.com/pycharm/)

I used helm, to install a postgres db on the minikube:

```Shell
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install postgres-local --set auth.postgresPassword=test bitnami/postgresql --namespace mealsapp-local --create-namespace
```

In a separate window, keep this running:

```Shell
kubectl port-forward --namespace mealsapp-local postgres-local-postgresql-0 5432:5432

```
Then create databases in postgres:

```Shell
psql --host 127.0.0.1 -U postgres -d postgres -p 5432
create database mealsappdb;
create database testdb;
exit;
```

#### Python Dependencies

Install Python Packages from the python environment you use:

```Shell
pip install -r requirements.txt
```

#### Create objects in db

Delete the contents of alembic/versions folder but keep the folder, then:

```Shell
alembic revision --autogenerate
alembic upgrade head
```

After this, you can run the app from PyCharm, and can reach the app on http://127.0.0.1:8000/docs  
You can run all unittests by choosing Run -> Run... -> Pytest  
Or individually by clicking the green arrow next to the methods in the tests package.

## Updating Docker Image

After local testing, rebuild docker image:

```Shell
docker build -t andrewhorvath8/fastapimeals .  
```

And push to hub (after docker login):

```Shell
docker push andrewhorvath8/fastapimeals
```

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