# I don't know how to_do 2 ** 0.5
# now I have 2 ** 2 and 0.5 ** 0.5
# How can I take a second arg?

def add_numbers(*args):
    for arg in args:
        print(arg ** arg)

add_numbers(4, 0.5)



def add_numbers2(*args):
    print(sum(args))

add_numbers2(1,2,3,4,5)

