HOUR_CONVERTION = 60
DAY_CONVERTION = 1440
PER_DAY_CONVERTION = 24
PUMP_GALLON = 1000
GALLON_MINUTE = 2
PRECISION = 3
CEIL_UPPER = 1
GALLON_ONE = 5
GALLON_TWO = 100
NEVER_REACH = -1

def main():
     filename = input("Please enter the file name: ")
     try:
          out = open(filename, "r")
     except FileNotFoundError:
          print(f"Unable to open {filename}.") 
          return

     file = out.read()
     file_line = file.split("\n")

     count_line = 0
     for _line in file_line:
          count_line += 1
          minutes = int(count_line)
          hour = float(minutes / HOUR_CONVERTION)
          day = float(minutes / DAY_CONVERTION)
     
     sum_number = 0
     minute_one = 1
     minute_two = 0
     for number in file_line:
          number = int(number)
          gallon = sum_number / PUMP_GALLON * GALLON_MINUTE

          if gallon < GALLON_ONE:
               sum_number += number
               minute_one += 1

          if gallon < GALLON_TWO:
               sum_number += number
               minute_two += 1
               if minute_two > minutes:
                  minute_two = NEVER_REACH

          minutes_pump = int(sum_number / PUMP_GALLON + CEIL_UPPER)
          minutes_gallons = int(minutes_pump * GALLON_MINUTE)
          day_gallons = float(minutes_gallons * PER_DAY_CONVERTION)
          kwh = float(sum_number / PUMP_GALLON / HOUR_CONVERTION)

     print(f"Data covers a total of {round(hour, PRECISION)} hours")
     print(f"(That's {round(day, PRECISION)} days)\n")
     print(f"Pump was running for {minutes_pump} minutes, producing {minutes_gallons} gallons")
     print(f"(That's {day_gallons} gallons per day)\n")
     print(f"Pump required a total of {sum_number} watt minutes of power")
     print(f"That's {round(kwh, PRECISION)} kWh\n")
     print(f"It took {minute_one} minutes of data to reach 5 gallons.")
     print(f"It took {minute_two} minutes of data to reach 100 gallons.")

main()
