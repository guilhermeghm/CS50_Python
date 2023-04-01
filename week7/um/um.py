import re

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r'\b[uU][mM]\b'
    matches = re.findall(pattern, s)
    return len(matches)

if __name__ == "__main__":
    main()