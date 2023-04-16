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
    "water": 400,
    "milk": 500,
    "coffee": 400,
}

profit = 0


def serve_customer():

    def process_coins():
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    def is_transaction_successful(money_received, drink_cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if money_received >= MENU[user_input]["cost"]:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            global profit
            profit += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == 'off':
        print("Coffee Machine Off")
        return
    if user_input == 'report':
        print("-------")
        print(f"Water: {resources['water']}ml\n")
        print(f"Milk: {resources['milk']}ml\n")
        print(f"Coffee: {resources['coffee']}g\n")
        print(f"Money: ${profit}")
        print("-------")

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        print(f"It costs ${MENU[user_input]['cost']}")
        money_calculated = process_coins()
        if is_transaction_successful(money_calculated, MENU[user_input]['cost']):
            ingredients = MENU[user_input]["ingredients"]
            for ing in ingredients:
                if ingredients[ing] > resources[ing]:
                    print(f"Sorry there is not enough {ingredients[ing]}.")
                    break
            print(f"Here is your {user_input}. Enjoy!")




serve_customer()
