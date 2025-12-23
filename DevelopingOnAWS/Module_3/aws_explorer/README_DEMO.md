* go on aws explorer
* right click on lambda to create a new SAM template (Create Lambda SAM Application)
* select Hello World Lambda
* select Python 3.13
* provide a name for the stack **lambda-helloworld**
* generate code in the root level of this project
* in generated folder deploy sam template

```
sam deploy
```

* you can check SAM outputs to catch URL of API Gateway (Key HelloWorldApi)
* Call Lambda through API Gateway
* in generated folder delete sam template

```
sam delete --no-prompts
```