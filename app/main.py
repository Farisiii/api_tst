from fastapi import FastAPI
from app.api.endpoints import auth, services
from mangum import Mangum

# Create FastAPI instance
app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(services.router, prefix="/services", tags=["services"])

if os.getenv("VERCEL_ENV"):
    handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)