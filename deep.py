#implement a program that prompts the user for the answer to the Great Question of Life, the Universe and

def main ():
    

    # Say hello to the user and explain the program
    print("Hello","I am here to help you by telling you the answer to the Great Question of Life, the Universe and Everything.")

    # Ask the user for the answer to the Great Question of Life, the Universe and Everything
    answer = input("Please, tell me, what is the answer to the Great Question of Life, the Universe and Everything? ").strip()

    # Output the answer
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes! That is correct.")
    else:
        print("That is incorrect. The answer is 42.")
    

    # Say goodbye to the user
    print(f"I hope I've been helpful. Goodbye!")

    main()