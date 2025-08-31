# Create a program that prompts the user for input and then outputs :) or :( emojis

def convert(text: str) -> str:
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    # Ask the user name
    name = input("What's your name? ").strip().title()

    # Say hello to the user and explain the program
    print(f"Hello, {name}! I am here to help you by transcribing your happy or sad faces into emojis.")

    # Ask the user for a sentence with happy or sad faces
    sentence = input(f"Please {name}, tell me the sentence with :) or :( ").strip()

    # Output the sentence with emojis
    print("Here is your sentence:") 
    print(convert(sentence))

    # Say goodbye to the user
    print(f"I hope I've been helpful, {name}. Goodbye!")

if __name__ == "__main__":
    main()