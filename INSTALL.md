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
# .vscode/extensions.json
# .vscode/settings.json
# .prettierignore
# .prettierrc
# prettier.config.mjs

#--- ESLint 환경 구성
# .vscode/extensions.json
# .vscode/settings.json
# eslint.config.mjs

#--- TDD (Test Driven Development) 환경 구성
#---     https://pypi.org/project/pytest
#---     https://github.com/pytest-dev/pytest
uv  add  pytest  --dev
uv  add  pytest-cov  --dev
pytest  --version

# app/calculator.py
# tests/test_calculator.py
pytest
pytest  --cov=appl  tests/
pytest  --cov=appl  tests/  --cov-report=html

#--- Debugging 환경 구성

#--- dotenv 환경 구성

#--- Python Coding Convention













```

  