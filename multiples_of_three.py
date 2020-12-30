def multiples_of_three(l: list) -> list:
    new_list = []
    if type(l) == str:
        l = l.split(',')
    for el in l:
        try:
            if float(el)%3 == 0:
                new_list.append(int(el))
        except ValueError: pass
    return new_list


if __name__ == '__main__':
    while True:
        I = input("Введите список чисел через запятую\n")
        O = multiples_of_three(I)
        print(O+'\nВыход по ctrl+C\n')