import sys
import os
from PIL import Image, ImageOps

def main():
    #check the number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.(jpg|jpeg|png) output.(jpg|jpeg|png)")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    #validate file extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output must be .jpg, .jpeg, or .png")

    #check that input and output extensions match
    if input_ext != output_ext:
        sys.exit("Input and output must have the same extension")

    try:
        #open the input image
        photo = Image.open(input_file)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    #open the shirt image
    shirt = Image.open("shirt.png")

    #resize and crop the input photo to the same size as shirt.png
    size = shirt.size
    photo = ImageOps.fit(photo, size)

    #overlay shirt.png on the photo using its transparency as mask
    photo.paste(shirt, shirt)

    #save the result to the output file
    photo.save(output_file)


if __name__ == "__main__":
    main()
