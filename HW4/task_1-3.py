
x = input("Введіть довільне слово або число (ціле): ")
if (x.isdigit()):
    print("Ви ввели число " + x)
    y = int(x) % 2
    if (y == 0):
        print("Введене Вами число парне")
    else:
        print("Введене Вами число не парне")
elif (x.isalpha()):
    print("Ви ввели слово " + x)
    print("Введене Вами слово містить " + str(len(x)) + " знаків")
else:
    print("Введені некоректні дані")