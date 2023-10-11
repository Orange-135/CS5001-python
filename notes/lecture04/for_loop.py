my_string = "Hello for loops!"

for my_character in my_string:
    print(f"Character:{my_character}")

print(f"The value of my_character is now {my_character}")

HOW_HIGH_TO_COUNT = 10
for i in range(1, HOW_HIGH_TO_COUNT+1):
    print(f"Value:{i}")
 #   i-=1
  #  print(f"Modified:{i}")

for i in range(1, HOW_HIGH_TO_COUNT+1, 2):
    print(f"Value:{i}")

for i in range(HOW_HIGH_TO_COUNT):
    print(f"Value:{i}")

print(range(10))

print(list(range(10))) 