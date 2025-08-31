# Tip Calculator: calculates how much tip to leave based on meal cost and percentage

def dollars_to_float(d: str) -> float:
    """
    Convert a string formatted as $##.## into a float.
    Example: "$50.00" -> 50.0
    """
    return float(d.replace("$", ""))

def percent_to_float(p: str) -> float:
    """
    Convert a string formatted as ##% into a float (decimal).
    Example: "15%" -> 0.15
    """
    return float(p.replace("%", "")) / 100

def main():
    # Ask the user for meal cost
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Ask the user for tip percentage
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip
    tip = dollars * percent
    
    # Output the result (rounded to 2 decimals)
    print(f"Leave ${tip:.2f}")

    # farewell message
    print("Thank you! I hope I've been helpful 🙂")

if __name__ == "__main__":
    main()
