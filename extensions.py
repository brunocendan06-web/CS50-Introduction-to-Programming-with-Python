#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream.

def main():
    # ask the user for a file name
    input_file = input("Enter the file name: ").strip()

    # give the user the correct name with .gif
    if input_file.lower().endswith(".gif"):
        print("image/gif")
    # with jpg or jpeg
    elif input_file.lower().endswith(".jpg") or input_file.lower().endswith(".jpeg"):
        print("image/jpeg")
    # with png
    elif input_file.lower().endswith(".png"):
        print("image/png")
    # with pdf 
    elif input_file.lower().endswith(".pdf"):
        print("application/pdf")
    # with txt
    elif input_file.lower().endswith(".txt"):
        print("text/plain")
    # with zip
    elif input_file.lower().endswith(".zip"):
        print("application/zip")
    # else output application/octet-stream
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()