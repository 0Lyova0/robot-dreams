
x = input("enter data to decrypt: ")
for i in x:
    if i.isdigit() and int(i) % 2 == 0:
        print("You entered a number and it is even")
    elif i.isdigit() and int(i) % 2 != 0:
        print("You entered a number and it is not even")
    elif i.isalpha() and i.istitle() == True:
        print("You entered a uppercase letter")
    elif i.isalpha() and i.istitle() == False:
        print("You entered a lowercase letter")
    else:
        print("You entered a symbol")
