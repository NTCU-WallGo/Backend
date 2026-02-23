from fastapi import FastAPI
from .core import config

app = FastAPI()
config.addMiddleware(app)
@app.get("/")
def root():
    return {"message": "This is root!"}
@app.get("/api")
def main():
    return {"message": "Hello World"}
