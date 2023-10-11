import sys


def main(symbol, width, height):
    if width < 2 or height < 2:
        print("You need to enter the bigger values") 
    else:
        for row in range(height):
           if row == 0 or row == height - 1:
            print(f"{symbol}" * width)
           else:
            print(f"{symbol}" + " " * (width - 2) + f"{symbol}")
    
    
main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))