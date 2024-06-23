#!/bin/bash

sudo yum install -y amazon-efs-utils
sudo mkdir /mnt/efs
sudo chmod 777 /mnt/efs

sudo wget https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.rpm
sudo yum install -y ./mount-s3.rpm
sudo mkdir /mnt/s3
sudo chmod 777 /mnt/s3
