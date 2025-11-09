# README

## 주요 명령어

```bash
#--- Python 지정
cd  ~/work/standard
source  .venv/bin/activate              #--- Linux

.venv\Scripts\activate                  #--- Window
.venv\Scripts\deactivate 

#--- mainFastAPI 프로그램 실행
uvicorn  app.mainFastAPI:app  --reload  --host 0.0.0.0  --port=8000

http://127.0.0.1:8000 
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

#--- mainFlask 프로그램 실행
#---     https://wikidocs.net/105816
python  app/mainFlask.py

http://127.0.0.1:8001

#--- TDD (Test Driven Development)
pytest

```
