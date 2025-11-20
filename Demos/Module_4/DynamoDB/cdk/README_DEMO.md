# Demo


## Lambda Only

* Create a lambda with name

```
DynamoDB-S3Feeder
```

* take the zip file location that contains lambda code from cloudformation outputs
* create an S3 event notification on bucket eventnotification-demo-457664 with prefix
```
files/
```


* Go to Module_4/DynamoDB
* execute command
```
python upload_files.py
```
* check the lambda logs 
* check cloudwatch metrics to see how lambda scales

## DynamoDb Demo

* This demo demonstrates as well DynamoDB global tables
* Lambda will already be created in this mode
* Go to Module_4/DynamoDB
* execute command
```
python upload_files.py
```
* Demonstrate query feature and partition key vs sort key
* pick some users that have same last name to see it retrieves multiple rows

Table name

```
demo_employee
```
Partition key
```
LastName
```
Sort Key
```
FirstName
```

Employees that have the same last name

| Last Name | First Name |
| --------- | ---------- |
| Andrews   | Bonnie     |
| Andrews   | Darren     |
| Andrews   | Kim        |
| Barnes    | Randy      |
| Barnes    | Dennis     |
| Oconnell  | Brian      |
| Oconnell  | Summer     |
| Payne     | Debra      |
| Payne     | Louis      |

* show items have been replicated in ireland table
* create items from ireland and assess the user is created in Paris table (active/active configuration)

## Items to create manually

Item from Paris

```
{
  "LastName": {
    "S": "FromParis"
  },
  "FirstName": {
    "S": "Marc"
  },
  "Index": {
    "N": "200"
  },
  "UserId": {
    "S": "f90cD3E76f1A9b8"
  },
  "Sex": {
    "S": "Male"
  },
  "Email": {
    "S": "marc.fromparis@training.aws.com"
  },
  "Phone": {
    "S": "0176483654"
  },
  "DateOfBirth": {
    "S": "1982-12-03"
  },
  "JobTitle": {
    "S": "Cloud Architect"
  }
}
```
Item from Ireland

```
{
  "LastName": {
    "S": "FromIreland"
  },
  "FirstName": {
    "S": "Marc"
  },
  "Index": {
    "N": "201"
  },
  "UserId": {
    "S": "f90cD3E76f1A9h7"
  },
  "Sex": {
    "S": "Male"
  },
  "Email": {
    "S": "marc.fromireland@training.aws.com"
  },
  "Phone": {
    "S": "0176483654"
  },
  "DateOfBirth": {
    "S": "1982-12-03"
  },
  "JobTitle": {
    "S": "Cloud Architect"
  }
}
```

