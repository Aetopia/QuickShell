@echo off
py -OO -m PyInstaller main.py -p modules -n "QSH" --specpath "%TEMP%" --workpath "%TEMP%" --noconfirm --icon NONE --clean
timeout 5
