import random
random_number = random.randint(1,50)
user_guess = int(input("Welcome to the Guessing Game!\n"+
"I picked a number between 1 and 50. Try and guess!\n"))
print(f"Your guessed {user_guess}")
tries = 0
while (random_number != user_guess):
    tries+=1  
    if user_guess == random_number + 1 or user_guess == random_number - 1 :
        print("That was luncky!")
        user_guess = int(input(""))
    elif user_guess <= random_number + 4  and user_guess >= random_number - 4 :
        print("That was amazing!")
        user_guess = int(input(""))
    elif user_guess <= random_number + 6  and user_guess >= random_number - 6 :
        print("That was okay")
        user_guess = int(input(""))
    elif user_guess == random_number + 7 or user_guess == random_number - 7 :
        print("Meh.")
        user_guess = int(input(""))
    elif user_guess <= random_number + 9  or user_guess >= random_number - 9 :
        print("This is not your game.")
        user_guess = int(input(""))
    elif user_guess > random_number + 10  and user_guess < random_number - 10 :
        print("You are the worst guesser I've ever seen.")
        user_guess = int(input(""))
else:
    tries+=1    
    print(f"Congratulations. You figured it out in {tries} tries.")
    
    