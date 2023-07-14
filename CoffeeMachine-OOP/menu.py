from prettytable import PrettyTable, MSWORD_FRIENDLY, DEFAULT, PLAIN_COLUMNS, MARKDOWN, ORGMODE, SINGLE_BORDER, DOUBLE_BORDER

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=60, milk=250, coffee=24, cost=2.50),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.50),
            MenuItem(name="cappuccino", water=100, milk=200, coffee=24, cost=3.00),
        ]

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None and prints a message"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available. Let me know if you would like to look at the menu.")

    def show_menu(self):
        """Displays the full menu in an easy to read table format"""
        menu_table = PrettyTable()
        menu_table.field_names = ["Drink", "Price"]
        for item in self.menu:
            # Format the cost to display 2 decimal places
            cost_formatted = "${:.2f}".format(item.cost)
            menu_table.add_row([item.name, cost_formatted])
        menu_table.align = "l"
        menu_table.set_style(DOUBLE_BORDER)
        print(menu_table)