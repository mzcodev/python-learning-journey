from random import randint

rndm_system_num = randint(1,100)
print(rndm_system_num) # To test the code and quickly end the game after testing.
user_guess = None
total_guesses = 0
user_current_guess = 0
user_previous_guess = 0
chances = 0

print("Hello buddy, Welcome to the guessing game!")
user_ans = input('If you want the game to start, enter "start", and if you want to learn about the game instructions, enter "help": ').lower()
while(True):
    if(user_ans == "help"):
        print("\nIn this game, I\'m going to think of a number between 1 and 100, and you have to guess the number I\'m thinking of.")
        print("I should also tell you that you only have 10 chances to guess a number between 1 and 100 (guessing a number outside this range won’t reduce the total number of guesses).")
        print('On your first guess, if the number you guessed is within 10 numbers of the number I have in mind, I\'ll tell you "warm!"')
        print('But if the number you guessed is more than 10 numbers away from the number I have in mind, I\'ll tell you "cold!"')
        print('In the following guesses, if the number you guess is closer to my number than your previous guess, I\'ll tell you "warmer!"')
        print('And if your guess is farther from my number than your previous guess, I\'ll tell you "colder!"\n')
        user_ans = input('Now enter the word "start" to begin the game: ').lower()
    elif user_ans == "start":
        print("\nThe game has started, good luck!")
        break
    else:
        user_ans = input("\nPlease enter only one of those two words: ").lower()


while(True):
    user_guess = int(input('Please enter an Integer Number between 1-100: '))
    user_current_guess = user_guess
    total_guesses += 1
    chances += 1
    if user_guess < 1 or user_guess > 100:
        print("out of bound")
        total_guesses -= 1
        chances -= 1
        continue
    elif(chances == 10):
        print("\nYour chances are over, and you lost the game :(")
        print("Good luck next time!\n")
        break
    elif(user_guess == rndm_system_num):
        if(total_guesses == 1):
            print("\nGood Job, your guess is right in first try!")
        else:
            print("\nGood Job your guess is right")
            print(f"total guesses that you make: {total_guesses}")
        break
    elif(total_guesses == 1):
        if(abs(user_guess - rndm_system_num) <= 10):
            print("Warm!")
            print(f"You have {10 - chances} guesses left.")
        else:
            print("Cold!")
            print(f"You have {10 - chances} guesses left.")
    else:
        if(abs(user_current_guess - rndm_system_num) < abs(user_previous_guess - rndm_system_num)):
            print("Warmer!")
            print(f"You have {10 - chances} guesses left.")
        else:
            print("Colder!")
            print(f"You have {10 - chances} guesses left.")
    user_previous_guess = user_guess