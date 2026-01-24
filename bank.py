def main():
    #ask for a greeting
    greeting = input("Greeting: ").strip().lower()
    print (f"${value(greeting)}")


def value(greeting):
    #determine the price based on the greeting
    greeting = greeting.lower()
    if greeting.startswith(("hello")):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
 main()