def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6: 
        return False

    if s.isalnum() == False:
        return False

    if s[0].isdigit() == True or s[1].isdigit() == True: 
        return False

    for char in s:
        if char.isdigit():
            if char=='0':
                return False
            else:
                break

    for char in range(len(s)):
        if s[char].isdigit():
            if not s[char:].isdigit():
                return False

    else:
        return True
main()
