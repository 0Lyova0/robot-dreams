from datetime import datetime

def log_time(my_func):
    def wraper():
        print(f"Function {my_func.__name__}\nRun on: {datetime.today()}")
        my_func()
    return wraper


@log_time
def test_func():
    print("Hello world!")


test_func()