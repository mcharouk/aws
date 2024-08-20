## Installation

### Instructions

* [Binaries here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
* Java 17 or greater required
* Go to installation folder and execute 

```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

### Notes

* There is a docker image that does not work with Rancher Desktop
* It can be attached as a Maven Dependency too


## Commands

Create first table

```
aws dynamodb create-table --attribute-definitions AttributeName=LastName,AttributeType=S AttributeName=FirstName,AttributeType=S --table-name Employee --key-schema AttributeName=LastName,KeyType=HASH AttributeName=FirstName,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --region eu-west-3 --output json --endpoint-url http://localhost:8000
```

list-tables

```
aws dynamodb list-tables --endpoint-url http://localhost:8000 --region eu-west-3
```

put-item

```
aws dynamodb batch-write-item --request-items file://employee-list.json --endpoint-url http://localhost:8000 --region eu-west-3
```

get-item

```
aws dynamodb get-item --table Employee --key file://get-item-key.json --endpoint-url http://localhost:8000 --region eu-west-3
```

delete table

```
aws dynamodb delete-table --table Employee --endpoint-url http://localhost:8000 --region eu-west-3
```
