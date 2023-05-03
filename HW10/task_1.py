
def my_func(a: int) -> None:
    print (a, end=" ")
    if a == 0:
        return None
    return my_func(a - 1)

print("Enter number")
a = int(input())
my_func(a)