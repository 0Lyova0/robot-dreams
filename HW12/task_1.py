from datetime import datetime

def log_datetime(func):
    def wrapper():
        print(f"Name of function is: {func.__name__} \n Run on: {datetime.today()}")
        func()
    return wrapper

@log_datetime
def my_function():
    print("Some info")


my_function()