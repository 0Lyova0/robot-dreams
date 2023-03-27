def add_numbers(a, b):
    return a ** b

exp_numbers = add_numbers(2, 3)
print(exp_numbers)


def add_numbers2(a=2, b=5):
    return  a + b
print(add_numbers2())
