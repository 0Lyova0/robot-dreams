def log_datetime(func):
    def wrapper():
        print(f"{'=' * 10}")
        func()
        print(f"{'=' * 10}")
    return wrapper


@log_datetime
def my_function():
    print("Some info")

my_function()