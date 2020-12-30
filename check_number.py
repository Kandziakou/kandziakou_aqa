def check_number(number: str) -> str:
    check = 7
    try:
        return "Привет" if int(number)>check else "Число должно быть больше "+str(check)
    except ValueError:
        return "Это не число"


if __name__ == '__main__':
    while True:
        I = input("Введите число\n")
        O = check_number(I)
        print(O+'\nВыход по ctrl+C\n')