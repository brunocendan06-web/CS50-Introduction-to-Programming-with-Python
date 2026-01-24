#create a program that represents a fuel gauge

def main():
    #create a loop
    while True:
        #ask the user for the level of fuel in the tank
        fuel = input("Fraction: ").strip()
        try:
            percentage = convert(fuel)
            print(gauge(percentage))
            break
        except ValueError:
            print("Invalid fraction. Please enter a valid fraction")


def convert(fraction):
    try:
        #split the input into
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        raise ValueError

        #prevent all the invalid inputs
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if numerator > denominator or numerator < 0 or denominator < 0:
        raise ValueError("Numerator cannot be greater than denominator or negative")
    
    # Return rounded percentage
    return round((numerator / denominator) * 100)


def gauge(percentage):
    #calculate the percentage of fuel in the tank
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()