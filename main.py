def decimal_to_other_system(num):
    num_sys = int(input("Выбери систему счисления в которую хочешь перевести: "))
    result = ""

    while num != 0:
        result += str(num % num_sys)
        num //= num_sys

    return result[::-1]


print(decimal_to_other_system(123))
