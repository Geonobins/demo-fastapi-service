from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Version 1.0 Live"}
