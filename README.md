# Django-Start-Project
A template project

If you have to create it from zero

## install uv in global python
pip install uv

## init project
uv init

## create a venv
uv venv

## activate venv
.venv/scripts/activate

## add Django
uv add Django


## create a new django project
django-admin startproject project

## rename the main folder (powershell)
rename-item project -NewName backend

## add pytest
uv add --dev pytest

## add ruff
uv add --group lint ruff
