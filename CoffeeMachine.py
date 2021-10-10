from menu import MENU, resources

def getChange(amount, coin):
    amount = float(amount)
    if coin == "quaters":
        return amount * .25
    elif coin == "dimes":
        return amount  * .10
    elif coin == "nickles":
        return amount * .05
    elif coin == "pennies":
        return amount * .01

def chargeCoffee(amount, coffee_cost, coffee_name)-> bool:
    available =  extractResources( COF_MENU[coffee]['ingredients'])

    if available:
        if amount > coffee_cost:
            change = format(amount - coffee_cost, ".2f")
            print(f"Here is ${change} in change.\nHere is your {coffee_name} ☕️. Enjoy!")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.\n")
            return False
    else:
        print("Sorry not enough ingredidnts")
        return False

def extractResources(Cof_resources) -> bool:
    for key in Cof_resources:
        if key in COF_RES:
            if Cof_resources[key] <= COF_RES[key]:
                COF_RES[key] -= Cof_resources[key]
            else:
                return False
    return True

# Menu from menu file
COF_MENU = MENU
COF_RES  = resources

eog = False
total = 0

while eog != True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    print("Please insert coins\n")

    # Get the total amount
    quaters = getChange(input("How many quaters?: "), "quaters")
    dimes   = getChange(input("How many dimes?: "), "dimes")
    nickles = getChange(input("How many nickles?: "), "nickles")
    pennies = getChange(input("How many pennies?: "), "pennies")

    #Get amount then pass to function
    total += quaters + dimes + nickles + pennies

    # return True/False if amount is over/under
    over_price = chargeCoffee(total, COF_MENU[coffee]['cost'], coffee)

    if over_price:
        pass
    else:
        continue
