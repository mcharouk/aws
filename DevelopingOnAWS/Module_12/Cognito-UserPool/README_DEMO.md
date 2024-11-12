## User pool creation

* sign-in with email
* change password policy to something very simple
* No MFA
* Disable Self service account recovery (enabling it has no effect anyway)
* Enable self registration
* Allow confirmation by mail (Recommended options)
* add some required user attributes (birth date in format YYYY-MM-DD)
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

* in client app
  * app type  = other (it has an impact on authentication flows). Other removes all flows but refresh tokens
  * client app name
 ```
 UserPoolDemoApp
 ``` 
  * generate client secret
   * callback URL **AND** sign-out URL (in advanced app client settings)
```
http://localhost:8501/
```
  
  * activate scope with **email, openid and profile**. This will allow to get user attributes in id token (among them, groups that are used to authorize page access)


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
