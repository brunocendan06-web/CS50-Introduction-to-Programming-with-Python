# It prompts the user for the time and determines the meal based on the hour.

def main():
    # Ask the user for the time
    time_str = input("What time is it? ").strip().lower()
    
    # Call the convert function to turn the input string into a decimal number.
    time = convert(time_str)
    
    # Check if the time falls in any meal window.
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    # If the time is not within any meal window, print nothing.
    else:
        print("")

# This function converts a time string in to a decimal number.

def convert(time_str):
    # Handle "a.m." or "am" to clean the string before conversion.
    if "a.m." in time_str or "am" in time_str:
        # Replace the a.m. markers and clean up any extra spaces.
        time_str = time_str.replace("a.m.", "").replace("am", "").strip()
    
    # Handle "p.m." or "pm".
    if "p.m." in time_str or "pm" in time_str:
        # Replace the p.m. markers and clean the string.
        time_str = time_str.replace("p.m.", "").replace("pm", "").strip()
        
        # Split the string by ":".
        hours, minutes = time_str.split(":") if ":" in time_str else (time_str, '0')
        hours = int(hours)
        minutes = int(minutes)
        # Convert to 24-hour format by adding 12 hours.
        return hours + minutes / 60 + 12
    
    if ":" in time_str:
        hours, minutes = time_str.split(":")
        hours = int(hours)
        minutes = int(minutes)
        return hours + minutes / 60
    # If the input is just a number, convert it directly to float.

    else:
        return float(time_str)

if __name__ == "__main__":
    main()