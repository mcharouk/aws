* on primary bucket, go on management and a replication rule
* role to be specified is called

> s3-replication-role
 
* upload some files in primary bucket

to execute in module root directory

```
aws s3 cp testFiles s3://mcc-s3replicationdemo-primary-65757847/files --recursive
```

* objects might take a few seconds to be copied