# Given a user's age and resting heart rate,
# compute the range of heart rates that corresponds to each zone. 
def main():
    # To display zones to no more than 2 decimal places
    PRECISION = 2 
    # Get input
    age = float(input("Please enter your age: "))
    restHR = float(input("Please enter your resting heart rate: "))
    print("=======================================")
    # Use formula to caculate the max heart rate and reserve heart rate
    max_heart_rate = 208 - 0.7 * age
    reserveHR = max_heart_rate - restHR
    # Zoon is devided by the formula: restHR + reserveHR * precentage
    # Zone n is from Xn to Xn+1
    X1 = restHR + reserveHR * 0.5
    X2 = restHR + reserveHR * 0.6
    X3 = restHR + reserveHR * 0.7
    X4 = restHR + reserveHR * 0.8
    X5 = restHR + reserveHR * 0.93
    X6 = restHR + reserveHR
    # Print results
    print("Your heart rate reserve is:", round(reserveHR,PRECISION), "bmp")
    print(f"""Here is a breakdown of your zone:
Zone 1: {round(X1,PRECISION)}bmp to {round(X2,PRECISION)}bmp
Zone 2: {round(X2,PRECISION)}bmp to {round(X3,PRECISION)}bmp
Zone 3: {round(X3,PRECISION)}bmp to {round(X4,PRECISION)}bmp
Zone 4: {round(X4,PRECISION)}bmp to {round(X5,PRECISION)}bmp
Zone 5: {round(X5,PRECISION)}bmp to {round(X6,PRECISION)}bmp
    """)

main()
