import sys

#The input number is equal to the sum of the n natural numbers from 1 to n
#n is triangluar number
def main(input_number):
     i = 1
     sum_i = i
     triangluar_number = 0
     while sum_i <= input_number:
          i += 1
          sum_i += i
          triangluar_number += 1
     print(triangluar_number)

main(int(sys.argv[1]))
