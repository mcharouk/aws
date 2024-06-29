#!/bin/bash

image_name=lambda-c-function
region_name=eu-west-3
repository_name=637423642269.dkr.ecr.eu-west-3.amazonaws.com

aws ecr get-login-password --region $region_name | docker login --username AWS --password-stdin $repository_name
docker build --platform linux/amd64 -t $image_name:test .
docker tag $image_name:test $repository_name/$image_name:latest
docker push $repository_name/$image_name:latest

# docker run --platform linux/amd64 -p 9000:8080 lambda-c-function:test