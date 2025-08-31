def main():
    #ask for a greeting
    greeting = input("Greeting: ").strip().lower()

    #determine the price based on the greeting
    if greeting.startswith(("hello")):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else: 
        print("$100")

if __name__ == "__main__":
 main()