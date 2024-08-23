## User pool creation

* sign-in with email
* confirmation by mail
* add some required user attributes
* self hosted UI
  * callback URL **AND** sign-out URL

```
http://localhost:8501/
```
* in client app, activate profile scope with email and openid. This will allow to get user attributes in id token


## Run the application

* execute script generate-env-file.py
* command to start application (to execute in webapp folder)

```
streamlit run streamlit-app.py
```

## Sign-up

* birth date format is YYYY-MM-DD

## Cognito group creation

* group2 for page2
* admin for page3
* admin for settings