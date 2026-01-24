#create a program that expects exactly one command-line argument

import sys
import csv
from tabulate import tabulate

def main(): 
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")
    
    filename = sys.argv[1]

    #check the file
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            table = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    #first row is headers, rest are data
    headers = table[0]
    rows = table[1:]

    #print table using tabulate
    print(tabulate(rows, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()