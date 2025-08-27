from fastapi import FastAPI

app = FastAPI(title="SchemaKage", version="0.1")

@app.get("/")
def root():
    return {"message": "Welcome to SchemaKage 🚀"}

