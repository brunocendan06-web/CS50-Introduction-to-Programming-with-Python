#create a corde that converts camelCase to snake_case

def main():
    # ASK THE USER FOR CAMEL CASE INPUT
    camel = input("camelCase: ").strip()
    snake = ""

    # Loop to convert uppercase letters to _lowercase
    for words in camel:
        if words.isupper():
            snake += "_" + words.lower()
        else:
            snake += words

    print(snake)

if __name__ == "__main__":
    main()
