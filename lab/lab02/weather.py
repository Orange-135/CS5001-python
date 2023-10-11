# What is the difference between the highest ,
# and the lowest temperature values predicted for the 10 day forecast?
maxtemp = 47
mintemp = 25
#print result
print(f"The different between the highest and the lowest temperature values \
prdicted for the 10 days forecast is {maxtemp - mintemp} F.")

#What is the average temperature at noon,
# predicted for the 10 day forecast?
##list temperature at noon for 10 days
noontemp_10_days = [42,43,46,43,45,43,36,33,35,38]
a = sum(noontemp_10_days)/len(noontemp_10_days)
#print result
print("The average temperature at noon \
predicted for the 10 day forecast is", round(a,3),"F.")

# What is the highest temperature predicted for the 10 day forecast,
# converted from Fahrenheit to Celsius?
BASE = 32
CONVERSION_FACTOR = 5.0/9.0
TERMP_PERCISION = 2
#Use convert formula 
fahrenheit_maxtemp = maxtemp
celsius_maxtemp = (fahrenheit_maxtemp - BASE) * CONVERSION_FACTOR
#print result
print("The highest temperature predicted for the 10 day forecast converted\
 from Fahrenheit to Celsius is", round(celsius_maxtemp,TERMP_PERCISION), "C.")
