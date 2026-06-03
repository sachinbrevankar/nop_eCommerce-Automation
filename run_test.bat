@echo off

cd /d "E:\Python Automation\nop_eCommerce Automation"

call .venv\Scripts\activate

pytest -v -s -m "regression" --html=Reports\reports.html testCases/ --browser chrome

pause