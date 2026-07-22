from fastapi import FastAPI

app = FastAPI(
    title="SmartAttend AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "SmartAttend AI Backend Running 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "SmartAttend AI Backend"
    }