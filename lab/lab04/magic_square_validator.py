sum = 15
def enter(num1, num2, num3):
     if int(num1) + int(num2) + int(num3) == sum:
          True
          return int(num1) + int(num2) + int(num3) == sum
     else:
          False
     
def main():
     row_1 = input("Enter a magic number: \n")
     row_2 = input("")
     row_3 = input("")

     if enter(row_1[0], row_1[1], row_1[2]) and enter(row_2[0], row_2[1], row_2[2]) \
     and enter(row_3[0], row_3[1], row_3[2]) and enter(row_1[0], row_2[0], row_3[0]) \
     and enter(row_1[1], row_2[1], row_3[1]) and enter(row_1[2], row_2[2], row_3[2]) \
     and enter(row_1[0], row_2[1], row_3[2]) and enter(row_1[2], row_2[1], row_3[0]):
          print("This is a magic square!")
     else:
          print("Not a magic square!")


main()
