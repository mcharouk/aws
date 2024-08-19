* go on aws explorer
* right click on lambda to create a new SAM template
* change the stack name in the generated folder. Go to file samconfig.toml and change stack_name value to **lambda_helloworld** for example
* in generated folder deploy sam template

```
sam deploy
```

* in generated folder delete sam template

```
sam delete --no-prompts
```