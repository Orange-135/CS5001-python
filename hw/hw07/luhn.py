# Define the constants
TEN = 10
MINUSONE = -1
ONE = 1
TWO = 2
ZERO = 0

# Prompt the user to enter check numbers
check_nums = input("Please enter check numbers:\n")

def double_num(check_num):
    # Separate the digits of the check number and add them together
    one = int(check_num // TEN)
    two = int(check_num % TEN)
    return one + two

# Function to reverse the order of digits in a list
def reverse_list(check_num):
    return [int(digit) for digit in check_num[::MINUSONE]]

# Function to validate a list of numbers
def validate(num_list):
    sum_num = 0 
    for index, value in enumerate(num_list, start=ONE):
        if index % TWO == ZERO:
            value = value * TWO
            # If the doubled value is greater than or equal to ten, add its digits together
            if value >= TEN:
                value = double_num(value)
        # Add the current value to the sum of numbers
        sum_num += value
    if sum_num % TEN == ZERO:
        print("There are valid numbers.")  
    else:
        print("There are not valid numbers.")

def main():
    num_list = [] 
    # Loop through the check_nums string
    for n in check_nums:
        if not n.isdigit():
            print("Not a valid input.")
            return 
        else:
            num_list.extend(reverse_list(n))
    validate(num_list)

main()
