from app.services.planner_engine import generate_itineraries


def search_trip(request):
    if request.budget <= 0:
        return {
            "status": "INVALID_INPUT",
            "found_valid_solution": False,
            "ai_summary": "Il budget deve essere maggiore di zero.",
            "itineraries": [],
            "cheapest_found_price": None,
            "budget_difference": None
        }

    if not request.candidate_cities:
        return {
            "status": "INVALID_INPUT",
            "found_valid_solution": False,
            "ai_summary": "Devi indicare almeno una città candidata.",
            "itineraries": [],
            "cheapest_found_price": None,
            "budget_difference": None
        }

    if request.end_date <= request.start_date:
        return {
            "status": "INVALID_INPUT",
            "found_valid_solution": False,
            "ai_summary": "La data di fine viaggio deve essere successiva alla data di inizio.",
            "itineraries": [],
            "cheapest_found_price": None,
            "budget_difference": None
        }

    itineraries = generate_itineraries(request)

    ordered = sorted(
        itineraries,
        key=lambda item: item.total_price
    )[:5]

    if not ordered:
        return {
            "status": "NO_ROUTES_FOUND",
            "found_valid_solution": False,
            "ai_summary": (
                "Non ho trovato voli disponibili per costruire un itinerario "
                "con le tratte e le date selezionate."
            ),
            "itineraries": [],
            "cheapest_found_price": None,
            "budget_difference": None
        }

    valid = [
        item for item in ordered
        if item.within_budget
    ]

    cheapest = ordered[0]
    difference = cheapest.total_price - request.budget

    if valid:
        return {
            "status": "SUCCESS",
            "found_valid_solution": True,
            "ai_summary": (
                "Ho trovato almeno una soluzione compatibile con il budget. "
                "Le opzioni sono ordinate dalla più economica."
            ),
            "itineraries": ordered,
            "cheapest_found_price": cheapest.total_price,
            "budget_difference": difference
        }

    return {
        "status": "ONLY_OVER_BUDGET",
        "found_valid_solution": False,
        "ai_summary": (
            f"Ho trovato alcune soluzioni, ma nessuna rientra nel budget. "
            f"La più economica costa {cheapest.total_price}€, cioè "
            f"{difference}€ sopra il budget."
        ),
        "itineraries": ordered,
        "cheapest_found_price": cheapest.total_price,
        "budget_difference": difference
    }