@echo off

call :main > build_objs.log
exit /b

:main
python -c "from tools.ObjDBHelper import *; build_objects('.', 'Objects.json')"