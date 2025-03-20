# Stackset Demo

* create a stackset
* select Service-managed permissions. Explain difference between 2 options
* get the uri in CF outputs
* StackSet Name

```
stackset-demo-sqs
```

* in Stackset options, leave everything default
* deploy to organizational units
* Enter OU Id : get sandbox OU in AWS Organizations
* In regions
  * add eu-west-3 and eu-west-1
* Explain **maximum concurrent accounts** and **failure tolerance** but leave default values
* After clicking on submit, we can see 2 stacks have been created
* After stacks completion, go on target account to see sqs queue has been created
* Note : to update stack set via console, create a new cloudformation template, and change stackset details