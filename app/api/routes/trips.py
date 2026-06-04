from fastapi import APIRouter
from app.schemas.trip_schema import TripSearchRequest, TripSearchResponse
from app.services.trip_service import search_trip

router = APIRouter()


@router.post("/search", response_model=TripSearchResponse)
def search(request: TripSearchRequest):
    return search_trip(request)