from foo_class import Foo


def main():
    my_foo = Foo("A string for an argument")
    my_val = my_foo.return_a_sum(1, 2, 3)
    print(my_val)


main()
