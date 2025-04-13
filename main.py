def decimal_to_other_system(num):
    num_sys = int(input("Выбери систему счисления в которую хочешь перевести число: "))
    sys_alphabet = "++++++++++ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$&"
    result = ""

    while num != 0:
        if int(num) % num_sys > 9:
            result += sys_alphabet[int(num) % num_sys]
        else:
            result += str(int(num) % num_sys)
        num //= num_sys
    return result[::-1]


# функция реализована и работает, но стоило бы подумать как ее оптимизировать
def other_system_to_decimal():
    num_sys = int(input("напечатай из какой СС хочешь перевести число: \n"))
    num = input("выбери число которое хочешь перевести: \n")[::-1]
    sys_alphabet = "++++++++++ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$&"
    index_num = []
    result = 0

    for i in range(len(num)):
        if num[i] in sys_alphabet:
            index_num.append([sys_alphabet.index(num[i]), i])
        else:
            index_num.append([int(num[i]), i])
    for i in range(len(index_num)):
        result += index_num[i][0] * (num_sys**index_num[i][1])
    return result


def other_to_other_system():
    return decimal_to_other_system(other_system_to_decimal())


# заменить if else на реализацию через словарь ? {кнопка : функция}
def main():
    while True:
        choice = int(input("1 перевод из 10 в другую СС\n2 перевод из любой в 10 СС\n"
                       "3 перевод из любой в любую СС\nТВОЙ ВЫБОР(1 2 3):\n"))
        if choice == 1:
            print(f"РЕЗУЛЬТАТ: {decimal_to_other_system(int(input("Напечатай число, которое хочешь перевести: \n")))}")
        elif choice == 2:
            print(f"РЕЗУЛЬАТ: {other_system_to_decimal()}")
        elif choice == 3:
            print(f"РЕЗУЛЬАТ: {other_to_other_system()}")
        else:
            print("Неверно введена кнопка, попробуй еще раз\nПОДСКАЗКА - 1 2 3")
        print("\n\n")


main()
