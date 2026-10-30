def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Пустой список")
    return sum(numbers) / len(numbers)

def grade_bounds(grades: list[float]) -> tuple[float, float]:
    if not grades:
        raise ValueError("Пустой список")
    return min(grades), max(grades)