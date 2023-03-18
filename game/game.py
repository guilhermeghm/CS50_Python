#First attempt

# import random

# def main():
#     while True:
#         try:
#             level = int(input("Level: "))
#             randonNumber = random.randint(1, level)

#             while True:
#                 try:
#                     guess = int(input("Guess: "))
#                     if guess < randonNumber:
#                         print("Too small!")
#                     elif guess > randonNumber:
#                         print("Too large!")
#                     else:
#                         return(print("Just right!"))
#                 except ValueError:
#                     guess = int(input("Guess: "))
#         except ValueError:
#             level = int(input("Level: "))

# main()

import random

while True:
    level = input("Level: ")

    if not int(level.isdecimal()) or int(level) < 0:
        level = input("Level: ")

    guess = input("Guess: ")

    if not int(guess.isdecimal()) or int(guess) < 0:
        guess = input("Guess: ")

    randonNumber = random.randint(1, int(level))

    if int(guess) < randonNumber:
        print("Too small!")
    elif int(guess) > randonNumber:
        print("Too large!")
    else:
        print("Just right!")
        break