# implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.

def main():
    total = 50
    while total > 0:  # repeat until total is 0 or less
        print(f"Amount Due: {total}")
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:  # only accept these coins
            total = total - coin        # subtract if valid
        # if not valid, do nothing and loop again

    # when loop ends (total <= 0), show change
    print(f"Change Owed: {abs(total)}")

if __name__ == "__main__":
    main()