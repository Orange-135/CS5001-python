import sys

def main(height):
    sum_row = (height - 1) // 2

    if height % 2 == 0:
        print("Please enter a odd number.")
    else:
        for row in range (0, sum_row + 1):
            if row == 0:
               print(" " * sum_row + "*")
            elif row in range (1, sum_row):
               print(" "* (sum_row - row) + "/" + " " * (2 * row - 1) + "\\")
               row += 1
            elif row == sum_row:
                print("/" + "_" * (height - 2)+"\\")
        
main(int(sys.argv[1]))

