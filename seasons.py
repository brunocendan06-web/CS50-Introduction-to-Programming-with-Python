from datetime import date
import sys
import inflect

def main():
    dob_str = input("Date of birth (YYYY-MM-DD): ")
    dob = parse_date(dob_str)
    if not dob:
        sys.exit("Invalid date format")
    minutes = minutes_since(dob)
    print(to_words(minutes) + " minutes")

def parse_date(s):
    try:
        year, month, day = map(int, s.split('-'))
        return date(year, month, day)
    except:
        return None

def minutes_since(d):
    today = date.today()
    delta = today - d
    return round(delta.total_seconds() / 60)

def to_words(n):
    p = inflect.engine()
    return p.number_to_words(n, andword='').capitalize()

if __name__ == "__main__":
    main()
