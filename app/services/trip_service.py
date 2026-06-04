from app.services.planner_engine import MAX_MANUAL_STOPS, generate_itineraries


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
            "ai_summary": "Devi indicare almeno una destinazione intermedia.",
            "itineraries": [],
            "cheapest_found_price": None,
            "budget_difference": None
        }

    if len(request.candidate_cities) > MAX_MANUAL_STOPS:
        return {
            "status": "INVALID_INPUT",
            "found_valid_solution": False,
            "ai_summary": f"Puoi indicare al massimo {MAX_MANUAL_STOPS} destinazioni intermedie.",
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
                "Non ho trovato voli disponibili per costruire l'itinerario "
                "con le tratte e le date selezionate. Prova a ridurre il numero "
                "di tappe o a cambiare l'ordine degli aeroporti."
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
                "Ho costruito un itinerario che include tutte le destinazioni "
                "intermedie indicate, nell'ordine inserito."
            ),
            "itineraries": ordered,
            "cheapest_found_price": cheapest.total_price,
            "budget_difference": difference
        }

    return {
        "status": "ONLY_OVER_BUDGET",
        "found_valid_solution": False,
        "ai_summary": (
            f"Ho costruito un itinerario completo, ma supera il budget. "
            f"Costa {cheapest.total_price}€, cioè {difference}€ sopra il budget."
        ),
        "itineraries": ordered,
        "cheapest_found_price": cheapest.total_price,
        "budget_difference": difference
    }
