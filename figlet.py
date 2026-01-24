#create a program that create the input in asscii art

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    #case 1 random
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    #case 2 -f o --font
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font in fonts:
            figlet.setFont(font=font)
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Usage: python figlet.py [-f FONT]")

    #ask for text
    text = input("Input: ")

    #render the text
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()