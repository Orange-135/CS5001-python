import sys
def main(width, rep_time):
     nose_cone(width)
     if len(sys.argv) == 3:
          fuselage_no_striped(width, rep_time)
     else:
          fuselage_striped(width, rep_time)
     tail(width)
 
def nose_cone(width):
     if width % 2 != 0:
          n = int((width + 1) / 2)
          for i in range(0, n): 
             print(" " * (n - i) + "*" * (2 * i - 1))
     else: 
          n = int(width / 2)
          for i in range(0, n):
             print(" " * (n - i) + "*" * (2 * i))

def fuselage_no_striped(width, rep_time):
     for _ in range(0, width * rep_time):
          print("X" * width)

def fuselage_striped(width, rep_time):
     for _ in range(0,rep_time):
          for _ in range(0, width // 2):
               print("-" * width)
          for _ in range(0, width - width // 2):
               print("X" * width)

def tail(width):
     p = (width - 1)//3
     q = width - 2 * p
     for _ in range(0, p):
          print(" " * p, end = '')
          print("*" * q, end = '')
          print(" " * p)
          p -= 1
          q += 2
     print("*" * width)
     print("*" * width)

main(int(sys.argv[1]), int(sys.argv[2]))
