# Python 개발 환경 구성

  

## Install

```bash
#--- VSC(Visual Studio Code) 설치
# TBD

#--- uv 설치
# TBD

#--- GitHub Repository 복제
cd  ~/work
git  clone  git@github.com:ONEHO33/standard.git

#--- Python 설치
uv  python  install  3.12
uv  python  list

cd  ~/work/standard
uv  init
uv  venv  --python  3.12

#--- Pretter 환경 구성
# .vscode/extensions.json 파일
# .vscode/settings.json 파일
# .prettierignore 파일
# .prettierrc 파일
# prettier.config.mjs 파일

#--- ESLint 환경 구성
# .vscode/extensions.json 파일
# .vscode/settings.json 파일
# eslint.config.mjs 파일

#--- TDD (Test Driven Development) 환경 구성
#---     https://pypi.org/project/pytest
#---     https://github.com/pytest-dev/pytest
uv  add  pytest  --dev
uv  add  pytest-cov  --dev
pytest  --version

# app/calculator.py 파일
# tests/test_calculator.py 파일
pytest
pytest  --cov=appl  tests/
pytest  --cov=appl  tests/  --cov-report=html

#--- dotenv 환경 구성
uv  add  python-dotenv

#--- black, isort, flake8 환경 구성
# VSC에서 Shift_Command_P  >  Preferences: Configure Language Specific Settign  >  Python

# .vscode/extensions.json 파일
# .vscode/settings.json 파일
# flake8 extension 설정

uv  add  flake8  --dev
# .flake8 파일

# 파일 검사
flake8  main.py
flake8  app/calculator.py

#--- Debugging 환경 구성

```

  