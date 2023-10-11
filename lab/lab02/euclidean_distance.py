# Write a program called euclidean_distance.py that prompts the user 
# for four numerical values representing two 2-dimensional points 
# (so, x1, y1, x2, and y2) and then calculates the Euclidean distance
def main():
    PERSICION = 2
    x1 = float(input("enter x1: "))
    y1 = float(input("enter y1: "))
    x2 = float(input("enter x2: "))
    y2 = float(input("enter y2: "))
    import math
    euclidean_dis = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#print result
    print("The Euclidean distance is", round(euclidean_dis,PERSICION))
main()
