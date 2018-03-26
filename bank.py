import account


def main ():
    rate = int (input("Vvedite procentnuiu stavku: "))
    money = int(input("Vvedite summu: "))
    period = int(input("Vvedite pediod vedenia scheta v mesyacah: "))

    result = account.caclulate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "Сумма на счете в конце периода: ", result)

    if __name__ == "__main__":
        main()
