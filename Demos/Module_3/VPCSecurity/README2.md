# Demo

## VPC Security


### NACLs

Inbound : 

| rule | port | cidr      | action |
| ---- | ---- | --------- | ------ |
| 100  | 80   | 0.0.0.0/0 | ALLOW  |

Outbound

| rule | port       | cidr      | action |
| ---- | ---------- | --------- | ------ |
| 101  | 1024-65535 | 0.0.0.0/0 | ALLOW  |

### Security Group

Inbound

| port | cidr      |
| ---- | --------- |
| 80   | 0.0.0.0/0 |



## VPC Flow Logs
For VPC Flow logs
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Resource": "*"
    }
  ]
}
```

Trusted Policy
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "vpc-flow-logs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
} 
```