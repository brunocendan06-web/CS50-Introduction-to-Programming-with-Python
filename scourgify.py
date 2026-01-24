import sys
import csv

def main():
    #check that the user provided exactly 2 arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        #open input file
        with open(input_file, newline="") as infile:
            reader = csv.DictReader(infile)

            #open output file
            with open(output_file, "w", newline="") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    #defensive split
                    if ", " in row["name"]:
                        last, first = row["name"].split(", ")
                    else:
                        sys.exit("Invalid name format")

                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()