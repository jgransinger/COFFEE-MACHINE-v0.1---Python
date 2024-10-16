def drink_to_make(drink):
    if drink == 'cappuccino':
        print("You ordered a Cappuccino")
    elif drink == 'latte':
        print("You ordered a Latte.")
    elif drink == 'espresso':
        print("You ordered an espresso")
    elif drink == 'report':
        print(resources)
    elif drink == 'off':
        print("Machine powering off... Goodbye.")

def process_payment(drink):
    cost = MENU[drink]['cost']
    print(f"Please insert payment. ${cost} is required : ")
    dol = float(input("Enter amount of Dollar Bills: "))
    q = float(input("Enter amount of Quarters: "))
    d = float(input("Enter amount of Dimes: "))
    n = float(input("Enter amount of Nickels: "))
    p = float(input("Enter amount of Pennies: "))
    pay_inserted = dol + (q*0.25) + (d*0.10) + (n*0.05) + (p*0.01)
    print(f"You inserted ${pay_inserted}.")
    if pay_inserted > cost:
        print(f"Returning ${pay_inserted - cost} in change.")
        return 1
    elif pay_inserted < cost:
        print(f"More money is needed. Returning money. Start order again.")
    elif pay_inserted == cost:
        print("Exact change received.")
        return 1

def check_resources(drink):
    if process_payment(drink) == 1:
        print("Payment successful. Processing order.")
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if MENU[drink]["ingredients"]["milk"] > 0:
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        if resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0:
            print("Not enough ingredients available. Please refill machine. Refunding money")
            print(f"Current resource status: {resources}")
            return 0
        else:
            print(f"Machine's resources have been reduced. New levels: {resources}")
            print(f"Your {drink} has been poured. Enjoy!")
            return 1

def make_another_cup():
    another_cup = input("Would you like to make another cup? y/n : ")
    if another_cup == "y":
        new_drink_ordered = input("What drink would you like? type 'cappuccino', 'latte', or 'espresso': ")
        drink_to_make(new_drink_ordered)
        if check_resources(new_drink_ordered) > 0:
            make_another_cup()
    else:
        drink_to_make("off")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

## Start of Code

drink_ordered = input("What drink would you like? type 'cappuccino', 'latte', or 'espresso': ")
drink_to_make(drink_ordered)
if drink_ordered != "off":
    check_resources(drink_ordered)
    make_another_cup()



