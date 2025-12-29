# User Pool

## User pool creation

* Select Standard application with name
```
UserPoolDemoApp
```
* sign-in with email
* Enable self registration
* add some required user attributes (birth date in format YYYY-MM-DD)
* return URL
```
http://localhost:8501/
```
## User Pool update

* rename user pool to 

```
UserPoolDemo
```
* In App clients
  * Login Pages
    * In Allowed sign-out URLs

```
http://localhost:8501/
```
  * Client App Settings
    * activate scope with **email, openid and profile** (add profile)

## Show UserPools Config

* Authentication Methods
  * Password Policy
* Sign-in
  * MFA options 
  * Account recovery (in case of lost password)
* Sign-up
  * Attribute verification and user account confirmation : keep everything as default, will check email
* Extensions
  * it's where you can customize authentication flows with Lambda triggers
* Show Users when registered

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
* Assign user to the 2 groups
* log out and log in again to check effect
* show id token , it should be printed in console