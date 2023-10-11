import math

def main():
     """
   Runs demo functioons
   None -> None
     """
     my_returned_value = hello_function("World!")  
     print("My retuened value: ", my_returned_value) #如果没有return，返回值为none
    

     my_doubled_num = double_num(5)
     print(my_doubled_num)

     my_new_num = add_nums(my_doubled_num, double_num(3))
     print(my_new_num)
     print(add_nums(5, 7))

     no_arg_no_return()

     v1, v2, v3 = multi_value_return()
     print(v1)
     print(v2)
     print(v3)

     print(is_prime(9))
     print(is_prime(11))


def hello_function(my_argument):
     """
     Prints hello message with an argument
     String -> None
     """
     print("Hello", my_argument)

def double_num(number):
     """
     Double a number
     Number -> Number
     """
     return 2 * number

def add_nums(num1,num2):
     """
     Add two numbers
     Number Number -> Number
     """
     return num1 + num2


def no_arg_no_return():
     """
     print a string 
     None -> None
     """
     print("Here's an IO action with no return value")

def multi_value_return():
    """
    Return three values
    None -> Character Character Number
    """
    return 'a', 'b', 10.5


def is_prime(num):
    """
    Evaluate whether a number is prime
    Integer -> Boolean
    """
    for d in range(2, int(math.sqrt(num)+1)):
        if not num % d:
            return False
    return True


main()

main()
