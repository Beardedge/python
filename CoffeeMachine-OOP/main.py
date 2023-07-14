from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True

while is_on:
    try:
        choice = input(f"What would you like? ")
        if choice == "menu":
            menu.show_menu()
        elif choice == "shutdown-auth-5667":
            print("Beep boop. Powering down.")
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.process_coins
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                else:
                    continue
            else:
                continue
    except AttributeError:
        continue