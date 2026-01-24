#implement a program that prompts the user for names, one per line, until the user inputs control-d.

import inflect

def main():
    p = inflect.engine()
    names = []


    #loop add names to the list
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    #join the names
    person = p.join(names)
    print(f"Adieu, adieu, to {person}")

if __name__ == "__main__":
    main()