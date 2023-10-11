import sys
import math
def main():
     max = int(sys.argv[1])
     print(2)
     
     for i in range(3, max+1, 2):
          is_prime = False

          k=2
          while(k <= math.sqrt(i) and is_prime):
               if (i%k==0):
                    is_prime = True
               k+=1
          if (is_prime):
               print(i)

main()
