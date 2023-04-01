def main():
    gauge = get_value()
    if gauge <= 1:
        print("E")
    elif gauge >= 99:
        print("F")   
    else:
        print(f"{gauge}%")

def get_value():
    while True:
        try:
            value = input("Fraction: ")
            fuel = value.split('/')
            x = int(fuel[0])
            y = int(fuel[1])
            result = 100 * float(x)/float(y)
            if x > y:
                value = input("Fraction: ")
            return int(round(result))
        except (ValueError, ZeroDivisionError):
            value = input("Fraction: ")
        else:
            return result

main()