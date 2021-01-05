MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


is_on = True
profit = 0

while is_on:
    print("What would you like? (espresso/latte/cappuccino):")
    user_input = input()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink['ingredients']):
            print("Please insert coins.")
            quarters = float(input("How many quarters?"))
            dimes = float(input("How many dimes?"))
            nickles = float(input("How many nickles?"))
            pennies = float(input("How many pennies?"))
            monetary_value = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
            for item in drink['ingredients']:
                resources[item] = resources[item] - drink['ingredients'][item]
            print(resources)
            if monetary_value > drink['cost']:
                profit += drink['cost']
                change_left = monetary_value - drink['cost']
                print(f"Here is ${change_left} in change.")
            else:
                print("Sorry there is not enough money. Money refunded")
            print(f"Here is your {user_input} Enjoy!")
