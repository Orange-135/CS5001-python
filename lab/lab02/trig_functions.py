#write a program that prompts the user for an angle in degrees, 
# and prints out the sine and cosine values for the angle.
def main():
    angle = float(input("enter an angle: ")) 
    import math
    sin_angle = math.sin(math.radians(angle))
    cos_angle = math.cos(math.radians(angle))
    print(f"The sine of {angle} is", sin_angle)#print result
    print(f"The cosine of {angle} is", cos_angle)#print result
 
main()