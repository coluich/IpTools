@echo off
pyinstaller --noconfirm --onefile --console --icon "computer.ico" --name "IpTools" --add-data "IPCalculator.py;."  "main.py"
move "%~dp0dist\*.exe" "%~dp0"
del IpTools.spec /f /q
rmdir build /s /q
rmdir dist /s /q