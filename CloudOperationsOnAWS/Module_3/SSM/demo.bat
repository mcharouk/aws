set action=%~1

if "%action%"=="deploy" goto deploy
if "%action%"=="destroy" goto destroy

:deploy
cdk deploy --require-approval never
python activateSSMSessionLogging.py
goto eof
 
:destroy
python deactivateSessionLogging.py
cdk destroy -f
goto eof

:eof