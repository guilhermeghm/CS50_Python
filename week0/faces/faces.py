def main():
    text = input()
    print(convert(text))

replace = {':(': '🙁', ':)': '🙂'}

def convert(text):
    for key, value in replace.items():
        text = text.replace(key, value)
    return(text)

if __name__ == "__main__":
    main()
