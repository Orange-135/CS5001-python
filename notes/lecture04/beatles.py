band = ["Paul", "Pete", "John", "George"]
instruments = ["Bass", "Drums", "Vocals", "Guitar", "Trombone"]

print(band)
print(len(band))


print(instruments[1])
print(instruments[1:])
print(instruments[1:3])


print(band)
band[1] = "Ringo"
print(band)


my_string = "Hello string!"

print(list(my_string))

for member in band:
    print(f"Introducing {member}")

lineup = zip(band, instruments)

print(lineup)

# print(len(lineup))

# Converting to a list exhausts/empties
# the zip object
list_lineup = list(lineup)

# Iterating through a zip object exhausts/empties
# the zip object
# for member_instrument in lineup:
#     print(f"Member/instrument: {member_instrument}")

print(list_lineup)

for member_instrument in list_lineup:
    print(f"Member/instrument: {member_instrument}")

lineup1 = zip(range(10), band, instruments)
print(lineup1)#需要转化为list才有结果
# lineup2 = lineup1

# print("Lineup 1 converted to list:", list(lineup1))
# print("Lineup 2 converted to list:", list(lineup2))

print(list_lineup)
print(list_lineup[2])
print(list_lineup[2][1])
print(list_lineup[2][1][3])

print(instruments[-1])

for member in lineup1:
    print(member[0], member[1], member[2])

#zip 元组   