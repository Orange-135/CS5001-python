fruits = ["apple", "banana", "cranberry", "durian", 
           "etrog", "fig", "guava", "honeydew"]

print(fruits[1:5])

first_letters = [fruit[0] for fruit in fruits]
print(first_letters)

fruits_copy = [fruit for fruit in fruits]
print(fruits_copy)

my_string = "Hi there, I'm a string!"
print(list(my_string))

words = my_string.split(' ')
print(words)

join_words = '-'.join(words)
print(join_words)

my_num_string = "123456"
my_num_list = [float(element) for element in my_num_string]
print(my_num_list)

list_of_lists = [
                ['a', 'b', 'c', 'd', 'e'],
                [1, 2, 3, 4, 5, 6, 7, 8, 9,"hi there!"],
                ["apple", "banana", "cranberry"]
               ]

print(len(list_of_lists))
print(len(list_of_lists[1]))
print(list_of_lists[1][-1][3])
# print(len(list_of_lists[1][-2][3])) ======   no result
print(list_of_lists[1][-2])

new_list = []
new_list.append("cheese")
new_list.append("egg")
print(new_list)
new_list.append("coffee")
print(new_list)

new_list.insert(0,"yogurt")
print(new_list)
new_list.insert(2,"pasta")
print(new_list)

more_food = ["meat", "potatoes", "juice"]
#new_list.append(more_food)=======直接加整个list
#print (new_list)
new_list.extend(more_food)#转化为元素加进去
print (new_list)


print(new_list)

for element in new_list:
    print(element, end=' ')
print()
