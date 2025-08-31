#create a dictionary that stores the number of calories in each food item

def main():
    #ask  the user for a fruit
    fruit = input("Fruit: ").strip().lower()

    #create a dictionary with the number of calories in each fruit
    fruit_calories = {
        "apple": 130,
        "avocado": 50,  
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "tangerine": 50,
        "watermelon": 80
    }
    #The data has been taken from https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/nutrition-information-raw-fruits-vegetables-and-fish
    #output the number of calories in the fruit
    if fruit in fruit_calories:
        # Output the number of calories
        print(f"Calories: {fruit_calories[fruit]}")



if __name__ == "__main__":
    main()
