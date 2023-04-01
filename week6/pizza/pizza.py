import sys
import csv
from tabulate import tabulate

filename = sys.argv[1]

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) != 2:
    sys.exit("Too many command-line arguments")
elif not filename.endswith('.csv'):
    sys.exit("Not a CSV file")
try:
    with open(filename):
        pass
except FileNotFoundError:
    sys.exit("File does not exist")


with open(filename) as file:
    csvTable = csv.reader(file, delimiter=',')
    headers = next(csvTable)

    table = []
    for row in csvTable:
        table.append(row)

    print(tabulate(table, headers, tablefmt="grid"))
