from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Construct objects from the class
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False

    # TODO 1. Print report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # TODO 2. Check resources sufficient? & # TODO 3. Process coins & # Todo 4. Check transaction successful?
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Todo 5. Make Coffee
            coffee_maker.make_coffee(drink)
