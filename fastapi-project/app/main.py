from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD + Docker + Nginx + FastAPI Working!"}

@app.get("/hello/{name}")
def hi(name: str):
    return {"msg": f"Hello {name}! Welcome to DevOps 🚀"}
