from collections import OrderedDict
    
def main():
    shop_list = {}
    while True:
        try:
            item = input().upper()
            shop_list.setdefault(item, 0)
            shop_list[item] += 1
        except EOFError:
            shop_list_ordered = OrderedDict(sorted(shop_list.items()))
            for key, value in shop_list_ordered.items():
                print(value, key)
            break

main()