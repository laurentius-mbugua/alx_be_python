import random

# def guessing_game():
#     secret_number = random.randint(1, 10)
#     print("I'm thinking of a number between 1 and 10. Can you guess it?")
#     no_of_guesses = 0
#     guessed_correctly = False
#
#     while not guessed_correctly:
#         no_of_guesses += 1
#         guess = int(input("Guess the number"))
#
#         match guess:
#             case _ if secret_number == guess :
#                 print("Congratulations, you guessed it!")
#                 print("Your number of turns" , no_of_guesses)
#                 guessed_correctly = True
#             case _ if guess > secret_number:
#                 print("Your guess is too high,try again ")
#             case _ if guess < secret_number:
#                 print("Your guess is too low,try again ")
#             case _ :
#                 print("invalid input")
#
#     play_again = input("Would you like to play again? (y/n) ")
#     if play_again == ("y"):
#          guessing_game()
#     else:
#        print("Thanks for playing")
#
# guessing_game()

def loop_guessing_game():
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    no_of_guesses = 0
    guess = 0

    print(secret_number)
    while guess != secret_number:
        no_of_guesses += 1
        guess = int(input("Guess the number"))
        if guess < secret_number:
            print("Too low")
        else:
            print("Too high")
    print("you have guessed the correct number in ",no_of_guesses," guesses")

    play_again = input("Would you like to play again? (y/n) ")
    if play_again == ("y"):
        loop_guessing_game()
    else:
         print("Thanks for playing")

loop_guessing_game()



i = 5