# README

## 주요 명령어

```bash
#--- Python 지정
cd  ~/work/standard
.venv\Scripts\activate                  #--- Window
source  .venv/bin/activate              #--- Linux

#--- mainFastAPI 프로그램 실행
uvicorn  app.mainFastAPI:app  --reload

http://127.0.0.1:8000 
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

#--- TDD (Test Driven Development)
pytest

```
