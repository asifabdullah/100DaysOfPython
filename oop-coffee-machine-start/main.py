from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# menu_item = MenuItem(menu)


while is_machine_on:

    choice = input(f"\tWhat would you like? ({menu.get_items()}): ").lower()
    # print(choice)
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        # print(drink.cost)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
