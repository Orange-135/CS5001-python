#string
in_string = input("Please enter a string: ")

print(f"Your string is \"{in_string}\"") #in_string注释输出

print(f"Your string is {len(in_string)} characters long.") #in_string字符长度

print("your string in all caps is:")
cap_in_string = in_string.upper()
print(cap_in_string)#in_string转化为大写

print(f"your string in all lower is: {in_string.lower()}")#in_string 转化为小写


#以in_string = Hello Everybody!为例
print(in_string)#in_string直接输出

print(in_string[0])#in_string的第一个字符
print(in_string[1])#in_string的第二个字符
print (in_string[len(in_string)-1])#in_string的最后一个字符

print(in_string[-1])#in_string的倒数第一个字符
print(in_string[-2])#in_string的倒数第二个字符
print(in_string[-3])#in_string的倒数第三个字符

print(in_string[2:8])#in_string的第二个到第八个字符
print(in_string[2:12:2])#in_string的第二个到第十二个字符中步长相隔为二的字符
print(in_string[-1::-1])#in_string的倒数第一个到第一个字符中步长相隔为负一的字符=倒序输出
print(in_string[::])#in_string的第一个到第一个字符=不变
print(in_string[::3])#in_string的第一个到第一个字符中步长相隔为三的字符
print(in_string[-1::2])#in_string的倒数第一个到第一个字符=倒数第一个字符

print(f"The first intance of 'ry' appears at the position {in_string.find('ry')}" )
#从左向右找出在in_string中第一个出现ry的地方

print(f"The first intance of 'o' appears at the position {in_string.rfind('o')}")
#从右向左找出在in_string中第一个出现o的地方


#Example: 姓名的格式转化
fullname = input("Input your full name: ")

name_break = fullname.rfind(' ')

first_and_middles = fullname[:name_break]
last = fullname[name_break+1:]

print(f"Your name in last name format: {last},{first_and_middles}")


#Example: mutation
phrase = "Change is inevitable"

print("Original string:",phrase)
print("Length of string:",len(phrase))

mutation1 = phrase + "except from vending mechines"
print(f"1: {mutation1}")

mutation2 = mutation1.upper()
print(f"2: {mutation2}")

mutation3 = mutation2.replace(" ", "X")
print(f"3: {mutation3}")
print("Length of mutation3", len(mutation3))

mutation4 = mutation3 + "\n"
print(f"4: {mutation4}")
print("Length of mutation4", len(mutation4))#比3多一个字符

#直接将phrase[0] = "Z“不行，因为string inmutable