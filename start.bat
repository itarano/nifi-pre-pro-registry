@echo off & setLocal

for /f "delims=" %%x in (.env) do (set "%%x")

set parameters="%*"
if not x%parameters:registry=%==x%parameters% goto registry
if "%*"=="" goto registry
goto start-all

:registry
if exist volumes\nifi-registry\git ( rmdir /Q /S volumes\nifi-registry\git )
mkdir volumes\nifi-registry\git && cd volumes\nifi-registry\git && git clone https://github.com/itarano/%REGISTRY_FLOW_STORAGE%.git && cd ../../../ && goto start-all

:start-all
docker-compose up -d %*
goto done

:done
echo Done!

endlocal