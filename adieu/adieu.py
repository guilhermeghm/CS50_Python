import inflect

p = inflect.engine()

def main():
    nameList = []
    while True:
        try:
            names = input("Name: ")
            nameList.append(names)
        except EOFError:
            print()
            nameUpdatedList = []
            for name in nameList:
                nameUpdatedList.append(name)
                namesFormatted = p.join((nameUpdatedList))
                print(f"Adieu, adieu, to {namesFormatted}")
            break

main()