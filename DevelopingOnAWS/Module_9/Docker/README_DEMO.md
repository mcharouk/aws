## Pre-requisites

* start **rancher desktop**

## Build image

* go to **lambda** directory and execute

```
docker build --platform linux/amd64 -t lambda-on-docker-demo:latest .
```

## Test image locally

Run image
```
docker run --platform linux/amd64 -p 9000:8080 lambda-on-docker-demo
```

Test image

```
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{}"
```

## Upload image to ECR

* create ECR Repository with name **lambda-on-docker-demo**

* run script 

```
.\uploadToECR.bat
```


## Lambda

* create a lambda named **LambdaOnDockerDemo**
  * language : python 3.13
  * architecture : x86_64
  * role : provided by cf