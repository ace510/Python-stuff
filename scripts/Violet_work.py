import sys


def print_component():
    for component in sys.argv:
        print("My Name is")
        print(component)


print_component()


def do_Twice(f, v):
    f(v)
    f(v)


def print_String(string):
    print(string)


do_Twice(print_String, "Violet")
