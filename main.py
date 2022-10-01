from fastapi import FastAPI
app = FastAPI()

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Service is Online"}