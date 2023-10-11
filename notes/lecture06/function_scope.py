v = " this variable is defined globally"
MY_CONSTANT = 5

def main():
     f1("x value", "y vaule")
     print("Main:", v)#global scrope
     f2("Hello", "wiggly", "function")#constants" are stylistic only, not syntactic
     f3()
     print("Main:", v)

def f3():
     global v
     v= "F3 re-assigns global v"
     print("f3:", v)

def f2(x,y,z = "Default value"):
     print("f2:", x)
     print("f2:", y)
     print("f2:", z)

def f1(x,y):
     v = " Here is a v variable"
     print("f1:", x)
     print("f1:", y)
     print("f1:", v)

main()