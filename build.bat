@echo off

call :main > build\log.txt
exit /b

:main
python -c "from tools.ObjDBHelper import *; build_objects('objects', 'build/Objects.json')"
copy "stages\_Stages.json" "build\Stages.json"
