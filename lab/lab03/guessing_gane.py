#use random
import random
answer = random.randint(1,50)
#get input
guess_num = int(input("Welcome to the Guessing Game!\n"+
"I picked a number between 1 and 50. Try and guess!\n"))
times = 0
#use while and if 
while ( guess_num!= answer):
    times += 1
    if guess_num == answer + 1 or guess_num == answer -1:
        print("Your guess is scalding hot")
        guess_num = int(input(""))
    elif guess_num == answer + 2 or guess_num == answer - 2:
        print("Your guess is extremely warm")
        guess_num = int(input(""))
    elif guess_num == answer + 3 or guess_num == answer - 3:
        print("Your guess is very warm")
        guess_num = int(input(""))
    elif guess_num <= answer + 5 and guess_num >= answer - 5:
        print("Your guess is warm")
        guess_num = int(input(""))
    elif guess_num <= answer + 8 and guess_num >= answer - 8:
        print("Your guess is cold")
        guess_num = int(input(""))
    elif guess_num >= answer - 13 and guess_num <= answer + 13:
        print("Your guess is very cold")
        guess_num= int(input(""))
    elif guess_num <= answer + 20 and guess_num >= answer - 20:
        print("Your guess is extremely cold")
        guess_num = int(input(""))
    elif guess_num > answer + 20 or guess_num < answer - 20:
        print("Your guess is icy freezing miserably cold")
        guess_num = int(input(""))
else:
    times += 1
    print(f"Congratulations. You figured it out in {times} tries.")
