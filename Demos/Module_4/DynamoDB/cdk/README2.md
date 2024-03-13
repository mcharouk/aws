# Demo

## Lambda Configuration

lambda name

```
DynamoDB-S3Feeder
```

s3 prefix
```
files
```

* for Demo without DynamoDB, take the zip file location that contains lambda code from cloudformation outputs

## Upload Files

* Go to Module_4/DynamoDB
* execute command
```
python upload_files.py
```

## Dynamo Configuration

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

## Items to create manually

Item in Paris

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

