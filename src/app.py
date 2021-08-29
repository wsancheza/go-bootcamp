from fastapi import FastAPI
from routes.routes import greeting, wheather

app = FastAPI()
app.include_router(greeting)
app.include_router(wheather)

