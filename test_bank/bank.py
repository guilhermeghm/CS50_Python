def main():
    greeting = str.lower(input("Greeting: ")).strip()
    print(value(greeting))


def value(greeting):
    if greeting[0:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
