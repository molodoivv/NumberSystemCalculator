def decimal_to_other_system(num):
    num_sys = int(input("Выбери систему счисления в которую хочешь перевести число: "))
    result = ""

    while num != 0:
        result += str(int(num) % num_sys)
        num //= num_sys
    return result[::-1]

# функция реализована работает, но стоило бы подумать как ее оптимизировать
def other_system_to_decimal(num_sys, num):
    num_sys = num_sys.split()
    num = num[::-1]
    index_num = []
    result = 0

    for i in range(len(num)):
        index_num.append([int(num[i]), i])
    for i in range(len(index_num)):
        result += index_num[i][0] * (int(num_sys[0])**index_num[i][1])
    return result


print(other_system_to_decimal(input("выбери из какой системы в какую хочешь перевести"
                                    "(сначала в какой сс стоит потом в какую перевести)"
                                    "через пробел, пример: 10 2\n"),
                              input("выбери число которое хочешь перевести: \n")))
