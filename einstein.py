# Create a program that prompts the user for mass (kg) and outputs the equivalent energy (Joules) using Einstein's formula E = m * c^2

def energy(mass: int) -> int:
    """
    Calculate energy in Joules from mass in kilograms using E = m * c^2
    """
    c = 300000000  # speed of light in meters per second (m/s)
    return mass * c**2

def main():
    # Ask the user name
    name = input("What's your name? ").strip().title()
    
    # Say hello to the user and explain the program
    print(f"Hello, {name}! I will help you calculate energy (in Joules) from mass using Einstein's formula E = m * c^2.")
    
    # Ask the user for mass
    mass = int(input(f"Please {name}, enter the mass in kilograms: ").strip())
    
    # Calculate energy
    joules = energy(mass)
    
    # Output the result
    print("Here is the equivalent energy in Joules:")
    print(f"{joules} Joules")
    print(f"≈ {joules:.2e} Joules")
    
    # Say goodbye
    print(f"I hope I've been helpful, {name}. Goodbye!")

if __name__ == "__main__":
    main()
