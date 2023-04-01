import random

def main():
    counter = 10
    score = 0
    while True:
        try:
            userLevel = get_level()
            while counter > 0:
                x = generate_integer(userLevel)
                y = generate_integer(userLevel)
                userGuess = 3
                while userGuess > 0:
                    try:
                        userAnswer = x + y
                        problem = int(input(f"{x} + {y} = "))

                        if problem == userAnswer:
                            score += 1
                            break
                        else:
                            userGuess -= 1
                            print("EEE")
                    except ValueError:
                        userGuess -= 1
                        print("EEE")


                if userGuess == 0:
                    print(f"{x} + {y} = {userAnswer}")

                counter -= 1

            print(f"Score: {score}")
            break
        except (ValueError):
            pass

def get_level():
    userLevel = input("Level: ")
    if userLevel.isalpha() or int(userLevel) <= 0 or int(userLevel) > 3:
        input("Level: ")
    else:
        userLevel = int(userLevel)
        for level in [1,2,3]:
            if userLevel == level:
                return userLevel

def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    elif level == 3:
        integer = random.randint(100, 999)
    else:
        raise ValueError

    return integer


if __name__ == "__main__":
    main()