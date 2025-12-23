* who am i

```
aws sts get-caller-identity
```

* create bucket (help)

```
aws s3api create-bucket help
```

* create bucket (low-level api)

```
aws s3api create-bucket --generate-cli-skeleton
```

* create bucket (high-level api)

```
aws s3 mb s3://mcharouk-clidemo-867876
```

* upload some files

```
aws s3 cp testFiles s3://mcharouk-clidemo-867876/files --recursive
```

* list files

```
aws s3 ls s3://mcharouk-clidemo-867876 --recursive
```

* empty bucket

```
aws s3 rm s3://mcharouk-clidemo-867876 --recursive
```

* remove bucket (cli-skeleton)

```
aws s3api delete-bucket --generate-cli-skeleton
```

* remove bucket

```
aws s3api delete-bucket --cli-input-json file://delete-bucket.json
```


