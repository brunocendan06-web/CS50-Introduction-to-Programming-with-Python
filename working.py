import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'
    match = re.search(pattern, s)
    if not match:
        raise ValueError
    h1, m1, period1, h2, m2, period2 = match.groups()
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)
    if not (1 <= h1 <= 12) or not (0 <= m1 < 60):
        raise ValueError
    if not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError
    start_hour = h1 % 12 + (12 if period1 == "PM" else 0)
    end_hour = h2 % 12 + (12 if period2 == "PM" else 0)
    return f"{start_hour:02}:{m1:02} to {end_hour:02}:{m2:02}"

if __name__ == "__main__":
    main()
