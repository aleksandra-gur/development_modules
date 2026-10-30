def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Пустой список")
    return sum(numbers) / len(numbers)

def total(numbers: list[float]) -> float:
    return sum(numbers)