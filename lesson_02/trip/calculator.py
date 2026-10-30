from rich import print


def calculator():
    print("[bold cyan]Простой калькулятор[/bold cyan]")

    try:
        first = float(input("Введите первое число: "))
        operator = input("Введите операцию (+, -, *, /): ")
        second = float(input("Введите второе число: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            result = first / second
        else:
            print("[red]Неизвестная операция[/red]")
            return

        print(f"[green]Результат: {result}[/green]")

    except ValueError:
        print("[red]Ошибка: введите числа[/red]")
    except ZeroDivisionError:
        print("[red]На ноль делить нельзя[/red]")


if __name__ == "__main__":
    calculator()