from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
is_on = True
my_menu = Menu()
my_menu_item = MenuItem('name', 'water', 'milk', 'coffee', 'cost')

while is_on:
    print(my_menu.get_items())
    my_money_machine.report()
    my_coffee_maker.report()

    input_drink = input("Choose a drink:")
    menu_object = my_menu.find_drink(input_drink)
    cost_of_drink = menu_object.cost
    ingredients_of_drink = menu_object.ingredients
    name_of_drink = menu_object.name
    is_resource_for_drink = my_coffee_maker.is_resource_sufficient(menu_object)
    if is_resource_for_drink:
        print(f"Waiting for payment, its ${cost_of_drink}")
        acceptMoney = my_money_machine.make_payment(cost_of_drink)
        if acceptMoney:
            my_coffee_maker.make_coffee(menu_object)
