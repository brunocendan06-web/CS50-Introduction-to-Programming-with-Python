#create a program that read bitcoin value

import sys
import requests

def main():
    #check
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        #go to the dict
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request failed")
    #give total
    total = n * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()