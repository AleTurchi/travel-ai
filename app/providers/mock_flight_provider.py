from app.schemas.trip_schema import FlightOffer


def search_flights(origin, destination, departure_date):
    return [
        FlightOffer(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            price=80.0,
            airline="MockAir",
            duration_minutes=150
        )
    ]