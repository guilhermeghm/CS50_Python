camel = input("camelCase: ")

for letter in camel:
    if letter.isupper():
        camel = camel.replace(letter, "_" + letter.lower())
print(f"snake_case: ", camel)
