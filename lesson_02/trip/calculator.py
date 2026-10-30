def calculate_total(expenses):
    return sum(item["amount"] for item in expenses)


def calculate_average(expenses):
    if not expenses:
        return 0
    return calculate_total(expenses) / len(expenses)
