from datetime import date

from app.providers.serpapi_flight_provider import search_flights


flights = search_flights(
    "FCO",
    "AMS",
    date(2026, 8, 22)
)

print(flights)