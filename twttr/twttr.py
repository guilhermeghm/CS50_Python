twttr = input("Input: ")

for letter in twttr:
    if letter in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        twttr = twttr.replace(letter, "")
print(f"Output: ", twttr)
