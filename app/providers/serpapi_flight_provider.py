import os
import requests

from dotenv import load_dotenv
from app.schemas.trip_schema import FlightOffer

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def search_flights(origin, destination, departure_date):

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "outbound_date": str(departure_date),
        "currency": "EUR",
        "hl": "it",
        "type": "2",
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("STATUS:", response.status_code)
        print("BODY:", response.text)
        return []

    data = response.json()

    offers = []
    best_flights = data.get("best_flights", [])

    for flight in best_flights[:3]:
        price = float(flight.get("price", 0))
        flight_legs = flight.get("flights", [])

        airline = "UNKNOWN"
        departure_time = None
        arrival_time = None

        if flight_legs:
            first_leg = flight_legs[0]
            last_leg = flight_legs[-1]

            airline = first_leg.get("airline", "UNKNOWN")
            departure_time = first_leg.get("departure_airport", {}).get("time")
            arrival_time = last_leg.get("arrival_airport", {}).get("time")

        offers.append(
            FlightOffer(
                origin=origin,
                destination=destination,
                departure_date=departure_date,
                price=price,
                airline=airline,
                duration_minutes=flight.get("total_duration", 0),
                departure_time=departure_time,
                arrival_time=arrival_time
            )
        )

    return offers