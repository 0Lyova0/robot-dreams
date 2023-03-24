# 2 варіант мені подобається найкраще і match case беде виконувати свою головну ціль,
# але завдання полягає в "Створити програму, яка буде очікувати введення тексту від користувача"
# спробував написати через input без привязки до конкретних відповідей
# вийшло досить громістке і я не правильно прописав (не вистачає експірієнсу))))
# ідея полягала в тому що щоб розпізнати чи це текст чи цифри. якщо текст тоді ще 1 провірку на булеві значення
# якщо цифри тоді додаткова перевірка через прості арифметичні операції для визначення float чи int


x = input("choose one of the options (text; True; 2.5; 12345): ")

match x:
    case "text":
        print("Data which you entered has a type str")
    case "True":
        print("Data which you entered has a type bool")
    case "2.5":
        print("Data which you entered has a type float")
    case "12345":
        print("Data which you entered has a type int")
    case _:
        print("Incorrect data")



# x = True
#
# match x:
#     case _:
#         print (type(x))



# x = True  # examples "text" for str; True for bool; 2.4 for float; 12345 for int;
#
# match x:
#     case str():
#         print("Data which you entered has a type str")
#     case bool():
#         print("Data which you entered has a type bool")
#     case float():
#         print("Data which you entered has a type float")
#     case int():
#         print("Data which you entered has a type int")
#     case _:
#         print("Incorrect data")