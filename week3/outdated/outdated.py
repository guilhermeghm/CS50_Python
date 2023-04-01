monthsList = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    formattedDate = validate_date()
    print(formattedDate)

def validate_date():
    inputDate = input("Date: ").strip()

    while True:
        try:
            if (',') in inputDate and ("/") not in inputDate:
                inputDate = inputDate.split(', ')
                year = inputDate[1]
                monthDay = inputDate[0].split(" ")
                day = monthDay[1].zfill(2)
                monthIndex = monthsList.index(monthDay[0]) + 1

                if int(day) > 31:
                    inputDate = input("Date: ")
                formatted = f"{year}-{monthIndex:02}-{day:02}"
                return formatted

            elif ('/') in inputDate:
                if inputDate.isalnum():
                    inputDate = input("Date: ")

                inputDate = inputDate.split('/')

                for x in inputDate:
                    if " " in x:
                        inputDate = input("Date: ")

                month = inputDate[0].zfill(2)
                day = inputDate[1].zfill(2)
                year = inputDate[2]

                if int(day) > 31 or int(month) > 12:
                    inputDate = input("Date: ")

                formatted = f"{year}-{month}-{day}"
                return formatted

        except ValueError:
            inputDate = input("Date: ")
        else:
            continue

main()
