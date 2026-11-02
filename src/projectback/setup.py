from fastapi import FastAPI

from projectback.router import router

app = FastAPI()
app.include_router(router)
