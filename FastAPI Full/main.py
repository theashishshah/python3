from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return { "message": "server is running fine."}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}