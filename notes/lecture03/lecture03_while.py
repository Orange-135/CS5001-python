#while
while(True):
    in_string = input("Give me a string")
    print(in_string)
Print("All done")#和if不同，不会显示出来，


#条件语句和函数结合
def main():
    command = None
    while (command != 'stop'):
        command = in_lower("What do you want me to do ")
        print(f"okay, I'll {command}")
    print("Wow, Good to be done!")#一直循环

def in_lower(prompt):
    return input(prompt).lower()

main()
