import random

print("welcome to the game, this is a number guessing game! \n you got 5 attempts to guess the number between 1 and 100, let's start the game") 
number_to_guess = random.randrange(50, 100)

chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("please enter your guess: "))

    if my_guess == number_to_guess:
        print(f"the number is {number_to_guess} and you found it right {guess_counter} attempts")
        break
    
    elif guess_counter >= chances and my_guess != number_to_guess :

        print(f"Oops sorry, the number is {number_to_guess} better luck next time")

    elif my_guess > number_to_guess :
        print("try again, your guess is too high")

    elif my_guess < number_to_guess :
        print("try again, your guess is too low")





