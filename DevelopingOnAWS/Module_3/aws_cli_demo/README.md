* create bucket

```
aws s3 mb s3://mcharouk-clidemo-867876
```

* upload some files

```
aws s3 cp testFiles s3://mcharouk-clidemo-867876/files --recursive
```

* empty bucket

```
aws s3 rm s3://mcharouk-clidemo-867876 --recursive
```

* remove bucket

```
aws s3 rb s3://mcharouk-clidemo-867876
```