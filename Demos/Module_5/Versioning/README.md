# Demo

## Bucket name

* create bucket if it's not already there

```
marccharouk-demo-45756383
```

* Activate versioning if it's not the case
* upload sampleFile.txt

```
aws s3 cp sampleFile.txt s3://marccharouk-demo-45756383/sampleFile.txt
```

* edit the local file
* upload it again

```
aws s3 cp sampleFile.txt s3://marccharouk-demo-45756383/sampleFile.txt
```

* delete the file
```
aws s3 rm s3://marccharouk-demo-45756383/sampleFile.txt
```

* check markers
* to rollback delete operation, remove the delete marker
  
```
aws s3api delete-object --bucket marccharouk-demo-45756383 --key sampleFile.txt --version-id [DELETE_MARKER-VERSION]
```


