import sys

def main(height):
     even = height % 2
     half = height // 2
     # if input value is even
     if even == 0:
          #print the upper half of asterisks
         for i in range (half):
             print(" " * (half - i),end='')
             print("*" * (2 * i + 1))
          #print the upper half of asterisks
         for j in range (half):
             print(" " * (j + 1),end='')
             print("*" * (height - 2 * j - 1))
     # if input value is odd    
     elif even == 1:
          #print the upper half of asterisks
          for i in range (half + 1):
               print(" " * (half - i),end='')
               print("*" * (2 * i + 1))
          #print the upper half of asterisks
          for j in range (half):
               print(" " * (j + 1),end='')
               print("*" * (height - 2*j - 2))
           

main(int(sys.argv[1]))
     