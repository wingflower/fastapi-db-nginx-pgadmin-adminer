import uvicorn

from fastapi import FastAPI

from app.routes import index


app = FastAPI()
app.include_router(index.router)


@app.on_event("startup")
async def on_app_start():
    print("-----[Welcome]-----")


@app.on_event("shutdown")
async def on_app_stop():
    print("-----[Bye]-----")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10004, reload=True)
