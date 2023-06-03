from datetime import datetime


def num_of_repeads(my_func):
    print("How many times repeat func?")
    times = input()
    count = 1
    while count <= int(times):
        print(f"Function {my_func.__name__}\nRun on: {datetime.today()}")
        count += 1


@num_of_repeads
def test_func():
    print("Hello world!")


test_func()
