from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.trips import router as trips_router


app = FastAPI(
    title="Travel AI Backend"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://travel-ai-frontend-wheat.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    trips_router,
    prefix="/api/trips",
    tags=["Trips"]
)


@app.get("/")
def home():
    return {
        "message": "Travel AI Backend is running"
    }