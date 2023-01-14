from string import punctuation

def main():
    plate = input("Plate: ")
    if main(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    ...

def is_letters(plate):
    start = plate[0:2]
    if start.isalpha():
        return True
    else:
        return False

def size(plate):
    if (len(plate) >= 2 and len(plate) <= 6):
        return True
    else:
        return False

def check_numbers(plate):
    ...

def special_char(plate):
    if any(char in punctuation for char in plate):
        return False
    else:
        return True

def check_space(plate):
    if ' ' in plate:
        return False
    else:
        return True


main()



# for letter in twttr:
#     if letter in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
#         twttr = twttr.replace(letter, "")
# print(f"Output: ", twttr)
