from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from CI/CD FastAPI app!"}


@app.get("/health")
async def health():
    return {"status": "ok"}
