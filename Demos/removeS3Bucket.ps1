$bucketName="demo-marccharouk-76857485"
aws s3 rm s3://$bucketName --recursive
aws s3 rb s3://$bucketName