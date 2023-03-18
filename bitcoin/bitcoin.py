import requests
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif isfloat(sys.argv[1]) == False:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    jsonResponse = response.json()
    price = (jsonResponse["bpi"]["USD"]["rate"]).replace(",", ".").replace(".", "", 1)
    total = float(price) * float(sys.argv[1])
    print(f"${total:,.4f}")
except requests.RequestException:
    sys.exit()
