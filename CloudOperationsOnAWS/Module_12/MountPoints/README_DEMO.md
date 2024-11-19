## EFS mount

### EFS Creation

Create EFS with customize option
* all availability zone
* associate pre created security group

### EC2 script

* generate scripts to create and read file
* go in root directory

```
python generate-scripts.py
```

* in instance 1, copy/paste writeFile content in terminal
* in instance 2, copy/paste readFile content in terminal

## S3 mount

```
sudo -s
```

```
mount-s3 mountpoint-marccharouk-86758493 /mnt/s3 && \
cd /mnt/s3 && \
echo "Hello World" > HelloFromEC2.txt
```

* Check in S3 that file exists