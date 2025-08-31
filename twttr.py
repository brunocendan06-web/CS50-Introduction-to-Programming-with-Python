# Create a program that outputs the same text but with all vowels ommitted.

def main():
    # Ask the user for input
    text = input("Input: ")

    # Define a function to remove vowels
    vowels = "aeiouAEIOU"
    no_vowels = "".join([char for char in text if char not in vowels])
  
    # Output the text without vowels
    print(f"Output: {no_vowels}")

if __name__ == "__main__":
    main()