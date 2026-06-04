from datetime import date, timedelta

from app.providers.serpapi_flight_provider import search_flights
from app.schemas.trip_schema import Itinerary

MAX_MANUAL_STOPS = 7


def classify_trip(days_between_flights):
    if days_between_flights == 0:
        return "layover"

    if days_between_flights <= 2:
        return "short_stop"

    return "multi_destination"


def calculate_score(total_price, budget, days_between_flights):
    if budget <= 0:
        return 0

    price_score = 100 - ((total_price / budget) * 40)

    if days_between_flights == 0:
        stop_score = 5
    elif days_between_flights <= 2:
        stop_score = 10
    else:
        stop_score = 15

    return int(price_score + stop_score)


def normalize_airport_codes(codes):
    normalized = []

    for code in codes:
        value = code.strip().upper()

        if not value:
            continue

        if value not in normalized:
            normalized.append(value)

    return normalized


def build_route(origin, candidate_cities, final_destination):
    origin = origin.strip().upper()
    final_destination = final_destination.strip().upper()
    stops = normalize_airport_codes(candidate_cities)

    route = [
        origin,
        *stops
    ]

    if final_destination and final_destination != origin and final_destination not in route:
        route.append(final_destination)

    if route[-1] != origin:
        route.append(origin)

    return route


def build_leg_dates(start_date: date, end_date: date, number_of_legs: int):
    """
    Crea una data di partenza per ogni tratta.

    Esempio con rotta FCO -> PMI -> BCN -> AMS -> FCO:
    - tratta 1: start_date
    - tratte intermedie: distribuite tra start_date ed end_date
    - ultima tratta: end_date
    """
    if number_of_legs <= 1:
        return [start_date]

    available_days = (end_date - start_date).days

    dates = []

    for index in range(number_of_legs):
        if index == number_of_legs - 1:
            dates.append(end_date)
            continue

        offset = int((available_days * index) / (number_of_legs - 1))
        dates.append(start_date + timedelta(days=offset))

    return dates


def generate_itineraries(request):
    candidate_cities = normalize_airport_codes(request.candidate_cities)

    if len(candidate_cities) > MAX_MANUAL_STOPS:
        return []

    route = build_route(
        request.origin,
        candidate_cities,
        request.final_destination
    )

    number_of_legs = len(route) - 1
    leg_dates = build_leg_dates(
        request.start_date,
        request.end_date,
        number_of_legs
    )

    selected_flights = []

    for index in range(number_of_legs):
        origin = route[index]
        destination = route[index + 1]
        departure_date = leg_dates[index]

        offers = search_flights(
            origin,
            destination,
            departure_date
        )

        if not offers:
            return []

        cheapest_offer = min(
            offers,
            key=lambda offer: offer.price
        )

        selected_flights.append(cheapest_offer)

    total_price = sum(
        flight.price for flight in selected_flights
    )

    within_budget = total_price <= request.budget
    budget_difference = total_price - request.budget

    average_days_between_flights = 0
    if len(leg_dates) > 1:
        average_days_between_flights = int(
            (request.end_date - request.start_date).days / (len(leg_dates) - 1)
        )

    trip_type = classify_trip(average_days_between_flights)

    score = calculate_score(
        total_price,
        request.budget,
        average_days_between_flights
    )

    itinerary = Itinerary(
        cities=route,
        flights=selected_flights,
        total_price=total_price,
        score=score,
        trip_type=trip_type,
        within_budget=within_budget,
        budget_difference=budget_difference
    )

    return [itinerary]
