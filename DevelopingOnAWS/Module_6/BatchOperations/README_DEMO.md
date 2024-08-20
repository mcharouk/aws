# Batch Operations Demo

## Job creation

* for manifest format, specify CSV
* specify manifest file path

```
s3://demo-marccharouk-batchoperations-678474-files/manifest.csv
```
* Invoke Lambda function
* Select Invocation schema version 2.0
* Completion report

```
s3://demo-marccharouk-batchoperations-678474-files/completion-report
```
* In permissions choose **BatchOperationsRole**

## Job submission

* Once submitted, must Run job to confirm it. This confirmation is necessary when job is run from Console, but can be skipped if job is created by other means (SDK, CLI, etc...)