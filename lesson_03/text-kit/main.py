def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def main():
    text = input("Введите текст: ")

    print(f"Количество слов: {count_words(text)}")
    print(f"Количество символов: {count_characters(text)}")


if __name__ == "__main__":
    main()