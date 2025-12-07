from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"To Rohi": "Keep Smiling!"}
