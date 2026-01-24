#implement a program that prompts the user for a str in English and then outputs the “emojized” 

#import emoji pack

import emoji

def main():
    # input valid emoji name
    text = input("Input: ")
    # output the emojis
    print("Output:", emoji.emojize(text, language="alias"))

if __name__ == "__main__":
    main()