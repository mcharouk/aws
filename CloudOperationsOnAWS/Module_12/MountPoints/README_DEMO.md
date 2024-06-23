## EFS mount

### EFS Creation

Create EFS
* all availability zone
* associate pre created security group

### EC2 script

```
sudo -s
```

Instance 1

```
EFS_ID='fs-0a7a2c4b799cb4275.efs.eu-west-3.amazonaws.com'
sudo mount -t efs -o tls $EFS_ID:/ /mnt/efs
echo "Hello From EFS" > /mnt/efs/HelloFromEFS.txt
```

Instance 2

```
EFS_ID='fs-0a7a2c4b799cb4275.efs.eu-west-3.amazonaws.com'
sudo mount -t efs -o tls $EFS_ID:/ /mnt/efs
ls -l /mnt/efs
cat /mnt/efs/HelloFromEFS.txt
```

* Create a file on one instance, check that the other instance can read it

## S3 mount

```
sudo -s
```

```
mount-s3 mountpoint-marccharouk-86758493 /mnt/s3
cd /mnt/s3
echo "Hello World" > HelloFromEC2.txt
```