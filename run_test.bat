@echo off

cd /d "E:\Python Automation\nop_eCommerce Automation"

call .venv\Scripts\activate

pytest -v -s --html=Reports\reports.html testCases/test_deleteCustomer.py --browser chrome

pause