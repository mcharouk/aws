# VPC Endpoints

## S3 gateway endpoint

```
aws s3api list-buckets --region eu-west-3
```

## SQS Interface Endpoint 

!! Should not work !!
```
aws sqs create-queue --region eu-west-3 --queue-name TestQueue
```

Should work (replace right DNS Name found in CloudFormation output)
```
aws sqs create-queue --region eu-west-3 --endpoint-url https://vpce-0166d920a2e0e79f3-oys7cma1.sqs.eu-west-3.vpce.amazonaws.com/ --queue-name TestQueue
```
