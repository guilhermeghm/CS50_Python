import sys
import inflect
from datetime import date, datetime

ie = inflect.engine()

def main():
    birthdate = input("Date of Birth: ")
    valid_date = validate_date(birthdate)
    days_difference = calculate_difference(valid_date)
    output = format_output(days_difference)
    print(output)

def validate_date(birthdate):
    try:
        input_date = date.fromisoformat(birthdate)
        return input_date
    except ValueError:
        sys.exit("Invalid Date!")

def calculate_difference(birthdate):
    today = date.today()
    days_diff = today - birthdate
    days_diff.days * 24 * 60
    return days_diff.days * 24 * 60

def format_output(minutes):
    minutes_text = ie.number_to_words(minutes, andword="")
    return minutes_text.capitalize() + " minutes"

if __name__ == "__main__":
    main()
