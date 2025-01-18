@echo off
start python main.py
timeout /t 2 /nobreak > nul
start python invade_auto.py
