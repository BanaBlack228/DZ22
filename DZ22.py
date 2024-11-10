def main():
    name = input("Введите ваше имя: ")

    try:
        number = int(input("Введите число: "))

        if number < 0:
            print("Ошибка: число должно быть неотрицательным.")
        else:
            for _ in range(number):
                print(name)

    except ValueError:
        print("Ошибка: пожалуйста, введите корректное целое число.")


if __name__ == "__main__":
    main()

def main():
    months = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }

    try:
        number = int(input("Введите число от 1 до 12: "))

        if number < 1 or number > 12:
            print("Ошибка: число должно быть в диапазоне от 1 до 12.")
        else:
            print(f"Месяц: {months[number]}")

    except ValueError:
        print("Ошибка: пожалуйста, введите корректное целое число.")


if __name__ == "__main__":
    main()

def main():

    user_input = input("Введите строку: ")

    length = len(user_input)

    print(f"Введенная строка: '{user_input}'")
    print(f"Количество символов в строке: {length}")


if __name__ == "__main__":
    main()
