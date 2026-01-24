#I want to create little mistery game its name is going to be: Detective Quest


#Im going to use pyfiglet as in the Problem Set 4
import pyfiglet

# Function to print text in a fancy font
def fancy_print(text, font=None):
    
    if font:
        banner = pyfiglet.figlet_format(text, font=font)
        print(banner)
    else:
        print(text)

def main():
    #GAME BANNER
    fancy_print("Dark Night in London", font="big")

    #little introduction
    print("Late at night, you receive a call about a murder at a welcome party in a luxurious penthouse in London.")
    print("The penthouse was full of people celebrating, but a body has been discovered in one of the rooms!")
    print("As the lead detective, you must investigate the penthouse, question the people present, and solve the case.\n")


    #set up the case
    case_data = setup_case()

    #let the user investigate rooms interactively 2 times
    print("Hmmm, which room should I investigate first?" )
    choose_room(case_data)

    print("Which room should I investigate next?")
    choose_room(case_data)

    show_clues(case_data)

    #let the user interrogate suspects interactively 2 times
    print("Who should I interrogate first?")
    choose_suspect(case_data)

    print("Who should I interrogate next?")
    choose_suspect(case_data)

    success = solve_case(case_data)

    if success:
        fancy_print("YOU SOLVED IT!", font="slant")
    else:
        fancy_print("GAME OVER", font="doom")

     #reveal motive of the culprit
    print("\nMotive:")
    print("Charlie, the security guy, committed the murder out of jealousy. The victim had discovered that Charlie was secretly in love with one of the guests.")

#setup the case
def setup_case():
    #creates a dict that store all the data for solve the game
    return {
        "suspects": ["Alice", "Bob", "Charlie"],
        "rooms": ["Living Room", "Kitchen", "Balcony", "Bedroom"],
        "clues": {
            "Living Room": "wine glass with fingerprints",
            "Kitchen": "knife missing from counter",
            "Balcony": "engagement ring",
            "Bedroom": "blood-stained knife" 
        },
        "descriptions": {
            "Alice": "The nosy neighbor, always peeking over windows.",
            "Bob": "The building's concierge, knows everyone comings and goings.",
            "Charlie": "The security guy, always around and knows the residents, he's always checking the cams."
        },
        #who commited the crime
        "culprit": "Charlie",
        "found_clues": []  #stores clues discovered by the user
    }

#let the user choose and investigate a room
def choose_room(case_data):
    
    room_names_lower = [room.lower() for room in case_data['rooms']]
    while True:
        room_input = input(f"Available rooms: {case_data['rooms']}\n> ").strip().lower()
        #make sure it use the dict
        if room_input in room_names_lower:
            room_index = room_names_lower.index(room_input)
            room = case_data['rooms'][room_index]
            clue = case_data['clues'][room]
            print(f"You investigate the {room} and find {clue}.")
            if clue not in case_data['found_clues']:
                case_data['found_clues'].append(clue)
            return room
        #prevent an error
        else:
            print("Invalid room. Please choose again.")

#let the user choose and interrogate a suspect
def choose_suspect(case_data):
   
    suspects_lower = [suspect.lower() for suspect in case_data['suspects']]
    while True:
        suspect_input = input(f"People present: {case_data['suspects']}\n> ").strip().lower()
        #make sure it use the dict
        if suspect_input in suspects_lower:
            index = suspects_lower.index(suspect_input)
            suspect = case_data['suspects'][index]
            
            #show the full description to the user
            print(f"You interrogate {suspect}: {case_data['descriptions'][suspect]}")
            
            #tell the user if the suspect look kind of nervous
            if suspect == case_data["culprit"]:
                print(f"{suspect} seems nervous! Something is off...")
            else:
                print(f"{suspect} seems calm and collected.")

            return suspect
        else:
            print("Invalid person. Please choose again.")

#show the user collected clues
def show_clues(case_data):
    
    if case_data['found_clues']:
        #print the clues
        fancy_print("Clues discovered so far:")
        for clue in case_data['found_clues']:
            print(f"- {clue}")
    #prevent error, if there is no clue
    else:
        print("No clues discovered yet.")

#final part, let the user solve the case
def solve_case(case_data):
    
    suspects_lower = [suspect.lower() for suspect in case_data['suspects']]
    while True:
        #make sure that the program understand the answer with the .strip and .lower
        guess_input = input("Who do you think is the culprit?\n> ").strip().lower()
        #make sure it use the dict
        if guess_input in suspects_lower:
            index = suspects_lower.index(guess_input)
            guess = case_data['suspects'][index]
            if guess == case_data["culprit"]:
                fancy_print("Correct! You solved the case!")
                return True
            else:
                fancy_print("Incorrect. Better luck next time.")
                return False
        #prevent error, if the suspect doesnt exist
        else:
            print("Invalid suspect. Please choose from the list.")

if __name__ == "__main__":
    main()