#!/bin/bash
yum update -y
yum install -y httpd.x86_64

sudo chkconfig httpd on
