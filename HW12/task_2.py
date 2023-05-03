def separation(somefun):
    def wrap():
        print(f"{'='*10}")
        somefun()
        print(f"{'='*10}")
    return wrap()

@separation
def test_func():
    print("Hello world!")

test_func
