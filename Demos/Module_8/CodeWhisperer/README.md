* [link to sonarQube vulnerabilities](https://rules.sonarsource.com/python/type/Vulnerability/RSPEC-5146/) 


* Example with simple csv file
```
# load the sample.csv file
# remove duplicates
# sort lines in alphabetical order
# save to sample_sorted.csv
```

* Example with Pandas
```
import pandas as pd

# load the sample-pandas.csv file
# remove duplicates
# sort lines in alphabetical order
# save to sample_sorted_pandas.csv
```

* Example with S3 Bucket
```
import boto3

bucket_name = "marc-charouk-codewhisperer-demo"
file_name = "sample.csv"

# create a s3 bucket in eu-west-3 region as LocationConstraint
# upload sample.csv to the bucket
# list the objects in the bucket and print their object keys
# empty the bucket
# delete the bucket
```