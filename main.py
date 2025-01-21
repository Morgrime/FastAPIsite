from fastapi import FastAPI
from uvicorn import run

from endpoints.user_endpoints import router as user_router

app = FastAPI()
app.include_router(user_router)

if __name__ == '__main__':
    run(app=app)