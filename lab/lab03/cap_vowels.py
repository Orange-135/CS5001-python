#firstly, turn all the characters into lowercase;
#  then replace the vowels in upper case 
string = input("Please enter a string: ").lower() 
list_str = list(string)
len_str = len(string)
vowel = ["a","e","i","o","u"]
i=0
while i < len_str:
    # check list_str[i], if vowel, replace list_str[i]
    if (list_str[i] in vowel):
        curr_char = list_str[i]
        list_str[i] = curr_char.upper()
    i  = i + 1
str1 =''.join(list_str)# turn list into str
print(str1)
