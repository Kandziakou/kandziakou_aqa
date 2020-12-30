def check_name(name: str) -> str:
    check = "Вячеслав"
    return "Привет, "+check if name == check else "Нет такого имени"

if __name__ == '__main__':
    while True:
        I = input("Введите имя\n")
        O = check_name(I)
        print(O+'\nВыход по ctrl+C\n')