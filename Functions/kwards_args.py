def print_numbers(*args):
    for num in args:
        print(num)


print_numbers(1, 2, 3, 4)


def print_names(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_names(name="Ashley", age=15)


def display(a, b, c):
    print(a, b, c)


args = (1, 3, 5)
display(*args)  # unpacking

kwargs = {"a": 1, "b": 3, "c": 5}
display(**kwargs)  # unpacking
