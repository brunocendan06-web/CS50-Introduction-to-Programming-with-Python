def main():
    ip = input().strip()
    print(validate(ip))

def validate(ip):

    parts = ip.split(".")


    if len(parts) != 4:
        return False

    for part in parts:

        if not part.isdigit():
            return False
        if part != "0" and part.startswith("0"):
            return False


        num = int(part)
        if num < 0 or num > 255:
            return False

    return True 

if __name__ == "__main__":
    main()
