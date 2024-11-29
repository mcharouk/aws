# Prerequisities

* Created by CF
  * Role : EC2ProductPolicyForServiceCatalogRole
  * Cloud Formation in a S3 bucket (link in CF output) 

# Portfolio creation

* Create a portfolio
* In portfolio action
  * Create a product
  * Create a launch constraint
  * Create an Access to allow administrator role
  * Associate Tag Options

# Product creation

Provisioned Product Name
```
LinuxApacheTestProductInstance
```

Get Last parameter store key values for linux AMIs. Run that on a Windows Shell

```
aws ssm get-parameters-by-path --path /aws/service/ami-amazon-linux-latest --query Parameters[].Name
```

AMI Parameter Store Key

```
/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64
```

# Links

[Service catalog reference architecture](https://github.com/aws-samples/aws-service-catalog-reference-architectures)