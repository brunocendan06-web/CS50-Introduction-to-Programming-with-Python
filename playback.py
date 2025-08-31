
# Create a progam that prompts the user for input and then outputs that same input, replacing each space with ...

def main():
    # Ask the user name
    name = input("what's your name?").strip().title()
    
    # Say hello to the user and explain the program
    print(f"Hello, {name}","I am here to help you by replacing each space with ... in any sentence you want me to.")

    # Ask the user for a sentence
    sentence = input(f"Please {name}, tell me the full sentence you want me to replace each space with ... : ").strip()

    # Output the sentence with ...
    print(f"Here is your sentence:") 
    print(sentence.replace(" ","...") )

    # Say goodbye to the user
    print(f"I hope I've been helpful, {name}. Goodbye!")

if __name__ == "__main__":
    main()