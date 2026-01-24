# Create a program that outputs the same text but with all vowels ommitted.

def main():
    # Ask the user for input
    text = input("Input: ")
    # Output the text without vowels
    print("Output:", shorten(text))

def shorten(word):
    # Define a function to remove vowels
    vowels = "aeiouAEIOU"
    return "".join([char for char in word if char not in vowels])
  
    
  

if __name__ == "__main__":
    main()