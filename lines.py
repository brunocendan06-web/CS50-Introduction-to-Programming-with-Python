#create  a program that count lines

import sys

def main():
    #check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    #check that file is python
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    #try to open file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    #count lines of code in the file
    count = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped == "" or stripped == "\n":  
            continue
        if stripped.startswith("#"): 
            continue
        count += 1
    #output count
    print(count)


if __name__ == "__main__":
    main()