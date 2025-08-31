# Create a progam that prompts the user for input and then outputs input in lowercase


def main():
    # Ask the user name
    name = input("what's your name?").strip().title()

    # Say hello to the user and explain the program
    print(f"Hello, {name}","I am here to help you by transcribing your sentences written in capital letters into lowercase letters.")

    # Ask the user for a sentence in capital letters
    sentence = input(f"Please {name}, tell me the full sentence that you want me to trancribe to lowercase letters: ").strip()

    # Output the sentence in lowercase letters
    print(f"Here is your sentence:") 
    print(sentence.lower())

    # Say goodbye to the user
    print(f"I hope I've been helpful, {name}. Goodbye!")


if __name__ == "__main__":
  main()