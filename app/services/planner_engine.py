from datetime import date, timedelta
from itertools import product

from app.config.airports import ANYWHERE_TEST, AIRPORT_GROUPS, COUNTRY_GROUPS
from app.providers.serpapi_flight_provider import search_flights
from app.schemas.trip_schema import Itinerary


MAX_MANUAL_STOPS = 7
MAX_ROUTE_VARIANTS = 50


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


def remove_duplicates(values):
    result = []

    for value in values:
        if value not in result:
            result.append(value)

    return result


def expand_location(value):
    normalized = value.strip().upper()

    if normalized == "ANYWHERE":
        return ANYWHERE_TEST

    if normalized in AIRPORT_GROUPS:
        return AIRPORT_GROUPS[normalized]

    if normalized in COUNTRY_GROUPS:
        airports = []

        for city in COUNTRY_GROUPS[normalized]:
            airports.extend(expand_location(city))

        return remove_duplicates(airports)

    return [normalized]


def expand_route_variants(candidate_cities, max_variants=MAX_ROUTE_VARIANTS):
    expanded_steps = []

    for city in candidate_cities:
        expanded = expand_location(city)

        if not expanded:
            continue

        expanded_steps.append(expanded)

    if not expanded_steps:
        return [[]]

    variants = []

    for combination in product(*expanded_steps):
        variants.append(list(combination))

        if len(variants) >= max_variants:
            break

    return variants


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


def build_itinerary(request, route):
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

        if origin == destination:
            return None

        offers = search_flights(
            origin,
            destination,
            departure_date
        )

        if not offers:
            return None

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

    return Itinerary(
        cities=route,
        flights=selected_flights,
        total_price=total_price,
        score=score,
        trip_type=trip_type,
        within_budget=within_budget,
        budget_difference=budget_difference
    )


def generate_itineraries(request):
    candidate_cities = normalize_airport_codes(request.candidate_cities)

    if len(candidate_cities) > MAX_MANUAL_STOPS:
        return []

    route_variants = expand_route_variants(candidate_cities)

    itineraries = []

    for route_variant in route_variants:
        route = build_route(
            request.origin,
            route_variant,
            request.final_destination
        )

        itinerary = build_itinerary(request, route)

        if itinerary is not None:
            itineraries.append(itinerary)

    itineraries.sort(key=lambda itinerary: itinerary.total_price)

    return itineraries[:10]