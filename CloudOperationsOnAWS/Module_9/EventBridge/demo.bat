set action=%~1

if "%action%"=="deploy" goto deploy
if "%action%"=="destroy" goto destroy

:deploy
cdk deploy --all --require-approval never
goto eof
 
:destroy
python cleanResources.py
cdk destroy -f --all
goto eof

:eof