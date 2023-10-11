import sys

first_number = 0
second_number = 1
original_steps = 2

def main(number):
    list = [first_number, second_number]
    i = 0
    while i in range(0, number - original_steps):
        #each number after that in the sequence should be the sum of the two numbers before it
        item = list[i] + list[i + 1]
        #add the new value in the list
        list.append(item)
        i += 1
    print(list)

main(int(sys.argv[1]))
