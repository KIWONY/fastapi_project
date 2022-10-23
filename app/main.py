from dataclasses import asdict

import uvicorn
from fastapi import FastAPI

from app.common.conf import conf
from app.database.conn import db
from app.routes import index, user


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()  # 환경변수에 따라 환경값을 가져온다.
    app = FastAPI()
    conf_dict = asdict(c)

    # 데이터베이스 이니셜라이즈
    db.init_app(app, **conf_dict)

    # 라우터 정의
    app.include_router(index.router)
    app.include_router(user.router)

    return app

# 앱 정의
app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)

"""
<< fastapi + uvicorn 실행 >>
uvicorn main:app --reload --host=0.0.0.0 --port=8000 
main : main.py -> 파일경로에 따라 app.main 경로 지정 해서 서버 구동
--host : 모든 접근이 가능하도록 하기 위해 0.0.0.0 입력
--reload : 코드 변경 시 자동으로 저장되어 재시작 됨 
--port : 원하는 접속포트
"""