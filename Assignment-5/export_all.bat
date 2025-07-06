@echo off
set PY=python
set SCRIPT=export_northwind.py

for %%t in (Customers Orders "Order Details" Employees) do (
    %PY% %SCRIPT% --table %%t
)
