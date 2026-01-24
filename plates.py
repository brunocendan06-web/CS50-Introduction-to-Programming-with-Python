# Create a program that checks if a vanity plate is valid.
 #conditions:
 # 1. starts with at least two letters
 # 2. max length of 6 characters and min length of 2 characters
 # 3. numbers at the end, if any. first number cannot be '0'    
 # 4. no periods, spaces, or punctuation marks

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6: # condition 2
        return False
    
    if not s[:2].isalpha():
        return False
    
    if not s.isalnum(): # condition 4
        return False
    
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0":  # condition 3
                return False
            if not s[i:].isdigit():  # condition 3
                return False
            break
    
    return True
      


if __name__ == "__main__":

    main()
