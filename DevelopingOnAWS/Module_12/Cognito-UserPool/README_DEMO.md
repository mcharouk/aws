## User pool creation

* sign-in with email
* confirmation by mail
* add some required user attributes
* change password policy to something very simple
* enable self registration
* Attribute verification and user account confirmation : keep everything as default
* message delivery : select Cognito, and leave default
* Cognito pool name

```
UserPoolDemo
```

* self hosted UI
  * domain name
```
mcharouk-user-pool-demo
```
  * callback URL **AND** sign-out URL (in advanced app client settings)
```
http://localhost:8501/
```
* in client app
  * client app name
 ```
 UserPoolDemoApp
 ``` 
  * generate client secret
  * activate scope with **email, openid and profile**. This will allow to get user attributes in id token


## Run the application

* execute script generate-env-file.py
* command to start application (to execute in webapp folder)

```
streamlit run streamlit-app.py
```

* [Call login to self-hosted UI](https://github.com/mcharouk/aws/blob/main/DevelopingOnAWS/Module_12/Cognito-UserPool/webapp/components/authenticate.py?plain=1#L210)

* [Get code grant and user tokens](https://github.com/mcharouk/aws/blob/main/DevelopingOnAWS/Module_12/Cognito-UserPool/webapp/components/authenticate.py?plain=1#L187)
* [Get access and id token with auth code](https://github.com/mcharouk/aws/blob/main/DevelopingOnAWS/Module_12/Cognito-UserPool/webapp/components/authenticate.py?plain=1#L74)



## Sign-up

* birth date format is YYYY-MM-DD

## Cognito group creation

* create 2 groups
  * **group2** for page2 
  * **admin** for page3 and settings
