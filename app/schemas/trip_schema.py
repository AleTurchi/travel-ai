from datetime import date
from typing import List
from pydantic import BaseModel


class TripSearchRequest(BaseModel):
    origin: str
    final_destination: str
    start_date: date
    end_date: date
    budget: float
    candidate_cities: List[str]


class FlightOffer(BaseModel):
    origin: str
    destination: str
    departure_date: date
    price: float
    airline: str
    duration_minutes: int
    departure_time: str | None = None
    arrival_time: str | None = None


class Itinerary(BaseModel):
    cities: List[str]
    flights: List[FlightOffer]
    total_price: float
    score: int
    trip_type: str
    within_budget: bool
    budget_difference: float


class TripSearchResponse(BaseModel):
    status: str
    found_valid_solution: bool
    ai_summary: str
    itineraries: List[Itinerary]
    cheapest_found_price: float | None = None
    budget_difference: float | None = None