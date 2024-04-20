import uvicorn

from dataclasses import asdict

from fastapi import FastAPI, Depends
from fastapi.security import APIKeyHeader

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

from starlette.requests import Request

# WebSocker Test
# from starlette.endpoints import WebSocketEndpoint
# from starlette.websockets import WebSocket

from app.database.conn import db
from app.common.consts import conf
from app.middlewares.token_validator import access_control
from app.middlewares.trusted_hosts import TrustedHostMiddleware

from app.routes import (
    index, auth, users
)


API_KEY_HEADER = APIKeyHeader(name="Authorization", auto_error=False)


def create_app():
    """

    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 미들웨어 정의
    app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=access_control)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=conf().ALLOW_SITE,
        allow_credentials=True,
        allow_methods=conf().ALLOW_METHODS,
        allow_headers=conf().ALLOW_HEADERS
    )
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=conf().TRUSTED_HOSTS, except_path=["/health"])

    # 라우터 정의
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/api")
    app.include_router(users.router, tags=["Users"], prefix="/api", dependencies=[Depends(API_KEY_HEADER)])

    return app


app = create_app()


@app.on_event("startup")
async def on_app_start():
    print("-----[Welcome]-----")


@app.on_event("shutdown")
async def on_app_stop():
    print("-----[Bye]-----")


# WebSocket Test
# @app.websocket_route("/ws")
# class MessagesEndpoint(WebSocketEndpoint):
#     encoding = "text"
#     last_time = 0
#
#     async def on_connect(self, websocket):
#         await websocket.accept()
#         print(f"[{time()}] connected: {websocket.client}")
#
#     async def on_receive(self, websocket: WebSocket, data) -> None:
#         self.last_time = float(data)
#         print(self.last_time)
#
#     async def on_disconnect(self, websocket, close_code):
#         print(f"[{time()}] disconnected: {websocket.client}")
#         print("delay:", time() - self.last_time)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10004, reload=True)
