# Напишете програма, която за дадена цифра
# (0-9), зададена като вход, извежда името
# на цифрата на български език.

try:
    n = int(input("Въведи цифра: "))
    if n == 1:
        print("{} -> {}".format(n, "Едно"))
    elif n == 2:
        print("{} -> {}".format(n, "Две"))
    elif n == 3:
        print("{} -> {}".format(n, "Три"))
    elif n == 4:
        print("{} -> {}".format(n, "Четири"))
    elif n == 5:
        print("{} -> {}".format(n, "Пет"))
    elif n == 6:
        print("{} -> {}".format(n, "Шест"))
    elif n == 7:
        print("{} -> {}".format(n, "Седем"))
    elif n == 8:
        print("{} -> {}".format(n, "Осем"))
    elif n == 9:
        print("{} -> {}".format(n, "Девет"))
    else:
        print("Цифрата не е между 1 и 9.")
except ValueError as err:
    print(err)