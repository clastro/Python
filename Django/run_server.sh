python -m venv Django # 가상환경이름(Django)

# Vscode에서 F1 입력후 Interpreter 선택하면 가상 변수 환경

# 가상 변수 활성화
pip install django
python -m pip install --upgrade pip
django-admin startproject shea
python manage.py runserver

cd shea
python manage.py runserver #서버 돌아감
