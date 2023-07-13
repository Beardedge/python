MENU = {
    "espresso": {
        "ingredients": {
            "water": 32,
            "coffee": 7,
        },
        "cost": 0.50,
    },
    "latte": {
        "ingredients": {
            "water": 60,
            "milk": 300,
            "coffee": 14,
        },
        "cost": 3.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 60,
            "milk": 300,
            "coffee": 14,
        },
        "cost": 3.50,
    },
    "americano": {
        "ingredients": {
            "water": 360,
            "coffee": 28,
        },
        "cost": 2.85,
    }
}
profit = 0
resources = {
    "water": 2000,
    "milk": 3000,
    "coffee": 500,
}


def processPayment():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def isSuccessful(moneyReceived, drinkCost):
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def enoughResources(reqIngredients):
    for item in reqIngredients:
        if reqIngredients[item] > resources[item]:
            print(f"There is not enough {item}, sorry.")
            return False
    return True
    
def makeCoffee(drinkChoice, reqIngredients):
    for item in reqIngredients:
       resources[item] -= reqIngredients[item]
    print(f"Here is your {drinkChoice} ☕, enjoy!")

isOn = True

while isOn:
    choice = (input("What would you like? (espresso/latte/cappuccino/americano)")).lower()
    if choice == "off":
        print("Beep boop. Powering down.")
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        continue
    try:
        drink = MENU[choice]
        if enoughResources(drink["ingredients"]):
            payment = processPayment()
            if isSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])
    except KeyError as e:
        print("I'm sorry, I didn't catch that.")
        continue


