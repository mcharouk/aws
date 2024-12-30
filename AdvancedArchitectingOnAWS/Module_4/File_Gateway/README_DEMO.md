# File Gateway Creation

* File Gateway name

```
FileGatewayDemo
```
* Host platform : EC2
* Select customize your settings (EC2 is already created by CF)
* IP Address : take public IP Address of file gateway appliance (CF outputs)
* Endpoint options : Publicly accessible
* Check the EC2 instance is not initializing
* Activate Gateway
* Wait until local disks finished preparing. Should not be too long

# create file share

* Choose the gateway
* Select NFS
* Select pre-created s3 bucket, ends with **filegateway-databucket**
* click on customize configuration
* IAM Role to select : **FileShareRole**
* show options during the demo
  * KMS encryption
  * VPC link to communicate with S3
  * Audit logs
  * Storage class
* When NFS is created, it's in updating status. Wait until it's in Available status (can take 1 min)
* If it's not available re-create it, but don't use customize configuration. Probably the policies for IAM Role have changed, must update the demo to make it work

# EC2 mount

```
sudo -s
```

```
cd /home/ec2-user  && \
mkdir filegateway
```

* copy cmd provided by file share and replace [MountPath] by

```
/home/ec2-user/filegateway
```

```
cd filegateway  && \
ls -l  && \
touch test.txt
```

* copy in s3 bucket can take 1 or 2 min as it's asynchronous

# Cache refresh

* create file directly in s3 bucket
* try to see the file in EC2 client (it should not appear)
* go on file share menu, and click on refresh cache
* wait 1 or 2 mins, should be able to see it in EC2 client
