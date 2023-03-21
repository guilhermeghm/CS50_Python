import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")
try:
    with open(sys.argv[1]):
        pass
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
else:
    students = []

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

    studentsSplit = []

    for student in students:
        tempDict = {}
        for key, value in student.items():
            if key == "name":
                name = value.split(", ")
                tempDict["first"] = name[1]
                tempDict["last"] = name[0]
            else:
                tempDict[key] = value
        studentsSplit.append(tempDict)

    with open(sys.argv[2], 'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader() 
        
        for row in studentsSplit:
            writer.writerow(row)
