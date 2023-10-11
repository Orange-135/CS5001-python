##dictionary
my_empty_dictionary = {}

my_fruit_counter = {
    'apples': 3,
    'oranges': 5,
    'bananas': 2,
    'kiwis': 0
}
print(my_fruit_counter['apples'])  #print the value of apples

my_fruit_counter['pears'] = 7
print(my_fruit_counter) #add pears

my_fruit_counter['apples'] += 1
print(my_fruit_counter)  #add 1 in the value of apples

print(my_fruit_counter.items())  #print pairs(a list of two tuples)
#mutable: list, dictionary(value), set, string
#immutable: tuple, dictionary(key)
print(my_fruit_counter.keys()) #print a list of keys
print(my_fruit_counter.values())#print a list of values

del my_fruit_counter['apples']
print(my_fruit_counter) #delete apples

fruits_by_count = sorted(
    my_fruit_counter.items(),
    key=lambda x: x[1],
    reverse=True
)
print(fruits_by_count) #according to the ordering of values from high to low, get a list of items

for fruit in fruits_by_count:
    print(fruit[0], fruit[1]) #fruit[0]: keys; fruit[1]: values

my_food_type = {
    "vegetables": [],
    "fruits": [],
    "meats": [],
}
my_food_type["fruits"].append("apples")
my_food_type["vegetables"].append("carrots")
my_food_type["fruits"].append("oranges")
print(my_food_type) #add

my_food_type["fruits"].remove("apples")
print(my_food_type) #remove

my_food_type["fruits"].append("grapes")
my_food_type["fruits"].append("kiws")
print(my_food_type)
print(my_food_type["fruits"][0]) #print the first in a list of value 

for food in my_food_type["fruits"]:
    food = "bubble gum"
    print(food) #change
print(my_food_type["fruits"]) # will not change

for (index, food) in enumerate(my_food_type["fruits"]):
    my_food_type["fruits"][index] = "bubble gum"
    print(index, food) #not change
print(my_food_type["fruits"]) #change

for index in range(len(my_food_type["fruits"])):
    my_food_type["fruits"][index] = "licorice"
    food = my_food_type["fruits"][index]
    print(index, food) #change
print(my_food_type["fruits"]) #change


##set
my_fruit_set = {"banana", "fig", "apple"} 

def check_for_fruit(fruit, fruit_set):
    if fruit in fruit_set:
        print("We have a", fruit)
    else:
        print("We don't have a", fruit)
check_for_fruit("banana", my_fruit_set)
check_for_fruit("watermelon", my_fruit_set)
check_for_fruit("fig", my_fruit_set)

my_fruit_set.remove("fig")
check_for_fruit("fig", my_fruit_set)

my_fruit_set.add("watermelon")
check_for_fruit("watermelon", my_fruit_set)

print(my_fruit_set) #set is not ordering(random)

my_empty_set = set()
#{}, will get wrong because python cannot distingish between distionary and set.
#set(), can add
my_empty_set.add("bologna")
print(my_empty_set)
