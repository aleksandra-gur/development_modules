def main():
    orders = [
        {"name": "Кофе", "price": 150},
        {"name": "Чай", "price": 100},
        {"name": "Капучино", "price": 200},
    ]

    total = sum(order["price"] for order in orders)

    print("Отчёт кафе")
    for order in orders:
        print(f'{order["name"]}: {order["price"]} руб.')

    print(f"Итого: {total} руб.")


if __name__ == "__main__":
    main()