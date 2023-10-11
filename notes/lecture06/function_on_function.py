def main():
     function_caller(f1)
     function_caller_arg(f2, "Hi there")
     print("***")
     function_caller(f3)
     print("***")
     function_caller(f3()) #先执行f3再执行function_caller

def function_caller(foo):
     print("I call a function")
     foo()  #foo = f1

def function_caller_arg(foo, arg):
     print("I call a function with an argument")
     foo(arg)

def f4():
    print("I'm function f4")


def f3():
    print("I'm function f3")
    return f4

def f2(some_string):
     print("I'm f2, and here's my argument:", some_string)

def f1():
     print("I'm function f1")

main()