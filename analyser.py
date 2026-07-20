# analyser.py
# Analyses expense data and assigns spending personality.
# Three steps: group → percentage → personality


def group_by_category(expenses):
    """
    Groups expenses by category and sums amounts.
    Example: two Food entries of ₹450 and ₹380 → {"Food": 830.0}
    """
    grouped = {}
    for expense in expenses:
        category = expense["category"]
        if category in grouped:
            grouped[category] += expense["amount"]
        else:
            grouped[category] = expense["amount"]
    return grouped


def calculate_percentages(grouped):
    """
    Converts grouped amounts to percentages of total.
    Example: Food ₹830 out of ₹3179 total → Food: 26.1%
    """
    total = sum(grouped.values())

    if total == 0:
        return {}

    percentages = {}
    for category, amount in grouped.items():
        percentages[category] = round((amount / total) * 100, 1)

    return percentages


def get_personality(percentages):
    """
    Rule engine — reads percentages, returns personality type.
    Returns a tuple: (name, description)
    """
    food  = percentages.get("Food", 0)
    subs  = percentages.get("Subscriptions", 0)
    shop  = percentages.get("Shopping", 0)
    utils = percentages.get("Utilities", 0)

    comfort = food + subs

    if comfort > 50:
        return ("Comfort Seeker 🛋️",
                "Over half your money goes to food and subscriptions. "
                "You prioritise daily comfort over saving.")

    elif shop > 35:
        return ("Impulse Buyer 🛍️",
                "Shopping dominates your spending. "
                "You tend to spend on wants more than needs.")

    elif utils > 40:
        return ("Homebody 🏠",
                "Most money goes to utilities and essentials. "
                "Life runs smoothly but little is left for enjoyment.")

    elif max(percentages.values(), default=0) < 35:
        return ("Balanced Saver ⚖️",
                "No single category dominates. "
                "You spread spending evenly — a healthy financial habit.")

    else:
        return ("Chaotic Spender 🌪️",
                "Spending is spread across many categories "
                "with no single clear pattern.")


def run_analysis(expenses):
    """
    Full analysis pipeline — one call does everything.
    Returns: grouped amounts, percentages, personality tuple.
    """
    grouped     = group_by_category(expenses)
    percentages = calculate_percentages(grouped)
    personality = get_personality(percentages)
    return grouped, percentages, personality