amount = 50

while amount > 0:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount = amount - coin
        if amount > 0:
            print(f"Amount Due: ", amount)
        else:
            print(f"Change owed: ", abs(amount))
    else:
        print(f"Amount Due: ", amount)
