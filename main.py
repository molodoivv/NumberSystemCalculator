def decimal_to_other_system():
    num = int(input("Напечатай число, которое хочешь перевести: \n"))
    num_sys = int(input("Выбери систему счисления в которую хочешь перевести число: "))
    result = ""

    while num != 0:
        result += str(int(num) % num_sys)
        num //= num_sys
    return result[::-1]


# функция реализована работает, но стоило бы подумать как ее оптимизировать
# не продумал про то, что в СС где основание > 9 вводятся буквы английского алфавита
def other_system_to_decimal():
    num_sys = input("выбери из какой системы в какую хочешь перевести"
                    "(сначала в какой сс стоит потом в какую перевести)"
                    "через пробел, пример: 10 2\n").split()
    num = input("выбери число которое хочешь перевести: \n")[::-1]
    sys_alphabet = 'ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$&'
    sys_alphabet_nums = [i for i in range(10, 66)]
    index_num = []
    result = 0

    for i in range(len(num)):
        if num[i] in sys_alphabet:
            index_num.append([sys_alphabet_nums[sys_alphabet.index(num[i])], i])
        else:
            index_num.append([int(num[i]), i])
    for i in range(len(index_num)):
        result += index_num[i][0] * (int(num_sys[0])**index_num[i][1])
    return result


def main():
    while True:
        choice = int(input('1 перевод из 10 в другую СС\n2 перевод из любой в 10 СС\n'
                       '3 перевод из любой в любую СС\nТВОЙ ВЫБОР(1 2 3):\n'))
        if choice == 1:
            print(f"РЕЗУЛЬТАТ: {decimal_to_other_system()}")
        elif choice == 2:
            print(f"РЕЗУЛЬАТ: {other_system_to_decimal()}")
        else:
            print("Неверно введена кнопка, попробуй еще раз\nПОДСКАЗКА - 1 2 3")
        print("\n\n")


main()
