from datetime import timedelta

from app.config.airports import ANYWHERE_TEST
from app.providers.serpapi_flight_provider import search_flights
from app.schemas.trip_schema import Itinerary


def classify_trip(days_between_flights):
    if days_between_flights == 0:
        return "layover"

    if days_between_flights <= 2:
        return "short_stop"

    return "multi_destination"


def calculate_score(total_price, budget, days_between_flights):
    price_score = 100 - ((total_price / budget) * 40)

    if days_between_flights == 0:
        stop_score = 5
    elif days_between_flights <= 2:
        stop_score = 10
    else:
        stop_score = 15

    return int(price_score + stop_score)


def generate_itineraries(request):
    results = []

    candidate_offsets = [0, 1, 2, 3]

    cities_to_search = []

    for city in request.candidate_cities:
        if city.upper() == "ANYWHERE":
            cities_to_search.extend(ANYWHERE_TEST)
        else:
            cities_to_search.append(city)

    for city in cities_to_search:
        for offset in candidate_offsets:
            middle_date = request.start_date + timedelta(days=offset)

            if middle_date >= request.end_date:
                continue

            first_legs = search_flights(
                request.origin,
                city,
                request.start_date
            )

            second_legs = search_flights(
                city,
                request.final_destination,
                middle_date
            )

            return_legs = search_flights(
                request.final_destination,
                request.origin,
                request.end_date
            )

            if not first_legs or not second_legs or not return_legs:
                continue

            first_leg = first_legs[0]
            second_leg = second_legs[0]
            return_leg = return_legs[0]

            total_price = first_leg.price + second_leg.price + return_leg.price

            within_budget = total_price <= request.budget
            budget_difference = total_price - request.budget

            trip_type = classify_trip(offset)

            score = calculate_score(
                total_price,
                request.budget,
                offset
            )

            itinerary = Itinerary(
                cities=[
                    request.origin,
                    city,
                    request.final_destination,
                    request.origin
                ],
                flights=[
                    first_leg,
                    second_leg,
                    return_leg
                ],
                total_price=total_price,
                score=score,
                trip_type=trip_type,
                within_budget=within_budget,
                budget_difference=budget_difference
            )

            results.append(itinerary)

    return results