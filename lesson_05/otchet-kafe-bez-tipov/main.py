from app.services.statistics import average, total

def main() -> None:
    numbers = [10, 20, 30]
    print("Сумма:", total(numbers))
    print("Среднее:", average(numbers))

if __name__ == "__main__":
    main()