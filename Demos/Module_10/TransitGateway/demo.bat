set action=%~1

if "%action%"=="deploy" goto deploy
if "%action%"=="destroy" goto destroy

:deploy
cdk deploy --require-approval never
goto eof
 
:destroy
python cleanResources.py
python cleanVPCPeering.py
cdk destroy -f
goto eof

:eof