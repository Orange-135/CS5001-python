import sys
import math
def circle(r):
   for x in range(0, 2*r):
     for y in range(0, 2*r): 
          chord = math.sqrt((x - r) ** 2 + (y - r) ** 2)
          if  chord < r:
               print("o", end="")
          else:
               print(" ", end="")
     print()

circle(int(sys.argv[1]))