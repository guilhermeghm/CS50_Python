def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i


    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock 

if __name__ == "__main__":
    main()