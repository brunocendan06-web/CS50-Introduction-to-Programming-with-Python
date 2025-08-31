# make a calculator

def main():
    
    # convert the numbers to float
    x = float(input("What´s x?"))
    y = float(input("What´s y?"))
    

    # get the operator
    operator = input("What´s the operator? (+, -, *, /)")

    # check the operator and perform the calculation
    if operator == "+":
        z = x + y
        print(f"{x} + {y} = {z}")
    elif operator == "-":
        z = x - y
        print(f"{x} - {y} = {z}")
    elif operator == "*":
        z = x * y
        print(f"{x} * {y} = {z}")
    elif operator == "/":
        if y == 0:
            print("Error: Division by zero is not allowed.")
        else:
            z = x / y
            print(f"{x} / {y} = {z}")

print("Thanks for using my program :) ")

if __name__ == "__main__":
    main()