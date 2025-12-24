## Layer

* execute buildLayerPackage.ps1 to create layer package. It's a zip file that contains the code in folder named python
* create the layer

```
aws lambda publish-layer-version --layer-name lambda-utils --description "My layer" --zip-file fileb://layer-package/layer-package.zip --compatible-runtimes python3.13 --compatible-architectures "x86_64"
```

## Create Lambda Function

Name function (for clean up script)

```
LambdaUsingLayer
```

* Python 3.13
* Use created iam role (LambdaLayerRole)
* Code to get on s3 (Cloudformation output)
* Execute the lambda to show it's not recognizing the dependencies
* Add the layer
* Execute the lambda