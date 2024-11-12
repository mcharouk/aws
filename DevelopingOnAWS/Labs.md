# Lab 1

## Description

* configure permissions on Cloud9 that will be used to execute commands (EC2 instance profile)
* check explorer in cloud9, by using EC2 instance as profile
* verify permissions by executing s3 commands
* add permissions to current user and check the effect on command (delete s3 bucket)

## Tasks

Analyzing Environment

* Sometimes 2 cmds are presented are options. Only one works, solution is at the end of the lab
* Change user to use instance profile (careful about the right region)
* query s3. Try to remove a bucket (it fails)
* Change iam permissions
* remove s3 bucket

!!! Try to launch .Net lab, they might contains specifics to connect with RDP to a Windows instance !!!


# Lab 2

## Description

It consists of 
* creating a bucket with waiters, check bucket existence, etc...
* upload a file
* uploading and downloading an object (byte array)
* activate static web hosting with aws cli
  * check that bucket variable **mybucket** has been correctly set
* Bonus : activate static web hosting with sdk

## Optional Task

upload S3 files

```
s3Client.upload_file(name, bucket, key, ExtraArgs={'ContentType': contentType})
print(f"uploaded {name} to key {key} and bucket {bucket}")
```

enable static web hosting

```
website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
}
s3Client.put_bucket_website(Bucket=bucket,WebsiteConfiguration=website_configuration)
```

update bucket policy

```
s3Client.put_bucket_policy(Bucket=bucket, Policy=bucket_policy)
```


# Lab 3 (DynamoDB)

## Description

* Interact with DynamoDB programmatically using low-level, document, and high-level APIs in your programs.
* Document and high level, only for Java and .NET. Document in lab and bean in bonus question.
* Create a table using waiters
* Load a table by reading JSON objects from a file.
* Query with projection expressions
* Scan and paginate
* Update items with conditional writes
* Using PartiQL

## Tasks

Straightforward Lab

# Lab 4

## Description

* Create a lambda function
* use Environment variables
* use Polly and upload the mp3 generated file in S3
* Publish function
* Invoke Lambda in multiple way (console, from CLI)
* Bonus : create remaining lambdas

## Tasks

### Invoking a function

Must add --cli-binary-format to make it work when json is directly input in command line.
Not necessary if payload is given in a json file

```
aws lambda invoke --function-name dictate-function --payload '{"UserId": "newbie","NoteId": "2", "VoiceId": "Joey"}' --cli-binary-format raw-in-base64-out response.txt
```

# Lab 5 

## Description

* create a REST API with a resource
* add a GET Method
* Map the response to limit the amount of data returned
* add a POST Method and configure some model validation
* add CORS Configuration and deploy in a stage

## Tasks

# Lab 6

## Description

* Create a user pool and app client
* add new users
* test user authentication
* configure API Gateway to use Cognito as authorizer
* use a swagger file to configure API Gateway
* test front end

## Tasks

* There is a step in Lab 6 where student can look at the code details that will identify a user with Cognito
* Apart from this, in the web app src code
  * the magic happened in src/Components/Auth/Accounts.js
  * There is the authenticate method defined in here
  * This method is called from src/Routes/Login.js where the web form is defined

# Lab 7

## Description

* Enable X Ray Tracing and logging in the lambda code
* create sub segment and add annotations
* enable X Ray tracing in SAM template
* deploy application with SAM
* analyze traces : search by HTTP Status code, search for exception
* fix the error and deploy again

## Tasks

* when selecting the X-Ray traces
  * we can see traces associated to delete function
  * we can click on different component.
  * On lambda function component, we have a sub segment that was created in the code (following lab instructions), with the annotations. We can see the annotations on the right panel in the tab "Annotations" when selecting the right sub segment
  * we can see that DynamoDB sub segment is in 5XX error, we can click on it, go to the tab "Exceptions" on the right panel. Here we can see the error related to IAM permissions