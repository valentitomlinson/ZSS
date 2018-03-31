usd = 56
euro = 60
funt = 100
kron = 7
forint = 4


def calculate_income(rate, money, month):
    if money <= 0:
        return 0

    for i in range(1, month + 1):
        money = round(money + money * rate / 100 / 12, 2)
    return money

currency = int(input("Укажите код валюты (доллары - 1, евро - 2, фунт стерлинг - 3, норвежская крона - 4, венгерский форинт - 5): "))

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму в рублях: "))
    period = int(input("Введите период ведения счета в месяцах: "))


    result = calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result, "рублей")


    if currency == 1:
        cache2 = round(money / usd, 2)
        print(" Валюта: доллары США")
    elif currency == 2:
        cache2 = round(money / euro, 2)
        print(" Валюта: евро")
    elif currency == 3:
        cache2 = round(money / funt, 2)
        print(" Валюта: фунт стерлинг")
    elif currency == 4:
        cache2 = round(money / kron, 2)
        print(" Валюта: норвежская крона")
    elif currency == 5:
        cache2 = round(money / forint, 2)
        print(" Валюта: венгерский форинт")
    else:
        cache = 0
        print("Неизвестная валюта")

    print(" Сумма в выбранной валюте:", cache2)


    if currency == 1:
        cache = round(result / usd, 2)
    elif currency == 2:
        cache = round(result / euro, 2)
    elif currency == 3:
        cache = round(result / funt, 2)
    elif currency == 4:
        cache = round(result / kron, 2)
    elif currency == 5:
        cache = round(result / forint, 2)
    else:
        cache = 0
        print("Неизвестная валюта")
    print(" Сумма к получению в выбранной валюте:", cache)

if __name__ == "__main__":
    main()