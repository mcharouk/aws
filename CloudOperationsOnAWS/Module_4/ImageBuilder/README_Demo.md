# Image Builder Demo

## Build Component

* Type : **Build**
* OS versions : **Linux 2023**
* Name : **ApacheComponent**
* Component Version : **1.0.0**

build script

```
name: ApacheInstall
description: This installs Apache on a server and start service on startup
schemaVersion: 1.0

phases:
  - name: build
    steps:
      - name: ApacheInstall
        action: ExecuteBash
        inputs:
          commands:
            - yum update -y
            - yum install -y httpd.x86_64
            - sudo chkconfig httpd on
```

## Test Component

* Type : **Test**
* OS versions : **Linux 2023**
* Name : **ApacheTestComponent**
* Component Version : **1.0.0**
* 
test script

```
name: TestApacheUp
description: this script will test if apache is up and running
schemaVersion: 1.0

phases:
  - name: test
    steps:
      - name: TestApacheUp
        action: ExecuteBash
        inputs:
          commands:            
            - |
              systemctl is-enabled httpd.service
              if [ $? -ne 0 ]; then
                 echo "httpd.service is not enabled"
                 exit 1 
              fi
              systemctl is-active httpd.service
              if [ $? -ne 0 ]; then
                echo "httpd.service is not running"
                exit 1
              fi
```

## Image Recipe

* Name : **ApacheRecipe**
* Version : **1.0.0**
* Base image : **Linux2023**
* Image Name : **Amazon Linux 2023 x86**
* Build Component : **OwnedByMe** -> **ApacheComponent** 
* Test Component : **OwnedByMe** -> **ApacheTestComponent** 

## Infrastructure Settings

* Name : **ApacheInfrastructure**
* IAM Role : **Provided by CloudFormation**
* Instance Size : **t3.micro**

## Distribution Settings

* Distribution Name : **ApacheDistribution**
* Additional region : **eu-west-1**

## Image Pipeline

* Name : **ApacheImagePublisherPipeline**
* Build Schedule : **Manual**
* Recipe : **Use Existing Recipe** -> **ApacheRecipe**
* Infrastructure : **Use Existing Infrastructure Configuration** -> **ApacheInfrastructure**
* Distribution Settings : **Use Existing Distribution Settings** -> **ApacheDistribution**

## Monitoring

* Click on Image on the left menu
* Click on the version

