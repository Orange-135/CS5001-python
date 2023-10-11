#Get input
name = input("Welcome to the DMV (estimated wait time is 3 hours) \nPlease enter your first, middle, and last name:\n")
bir_date = input("Enter date of birth (MM/DD/YY):\n")
#use random get the DL
import random
random_license = random.randint(1000000,9999999)
print("Washington Driver License\nDL",random_license)
#find the location of the blank space from the right
name_break = name.rfind(" ")
#last name is between blank space and the last character
last_name = name[name_break + 1:]
print("LN",last_name)
#first name is between the first character and blank space 
first_middle_name = name[:name_break]
print("FN",first_middle_name)
print("DOB",bir_date)
#find the location of "/" from the right
date_break = bir_date.rfind("/")
input_yy = bir_date[date_break +1:]
#replace input_yy
exp_date = bir_date.replace(f"{input_yy}","21")
print("EXP",exp_date)
