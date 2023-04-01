def main():
    twttr = input("Input: ")
    print(shorten(twttr))


def shorten(word):
    for letter in word:
        if letter in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
