$bucketName="demo-marccharouk-76857485"
aws s3 mb s3://$bucketName
aws s3 cp S3Assets s3://$bucketName --recursive