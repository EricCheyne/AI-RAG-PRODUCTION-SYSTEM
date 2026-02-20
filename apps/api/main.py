from fastapi import FastAPI

app = FastAPI(title="AI RAG API")

@app.get("/")
async def root():
    return {"message": "AI Document Intelligence Platform API"}
