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
profit=0
resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
}

# TODO 1:'print report'
# TODO 2:'check sufficient resource'


def check_resource(ordered_drink):
    for ingredients in ordered_drink:
        if ordered_drink[ingredients] > resources[ingredients]:
            return False
        else:
            return True

# TODO 3:'process coins'
# TODO 4:'check transition successful'


def process_coins():
    quarter = int(input("how many quarts?: "))*0.25
    dimes = int(input("how many dimes?: "))*0.10
    nickel = int(input("how many nickels?: "))*0.05
    pennies = int(input("how many pennies?: "))*0.01
    total = quarter + dimes + nickel + pennies
    return total


def transition_success(ordered_drink, total):
    if ordered_drink['cost'] > total:
        return False
    else:
        change = round(total - ordered_drink['cost'], 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += ordered_drink['cost']
        return True



# TODO 5:'make coffee'

def make_coffee(ordered_item ,selected_drink):
        for ingredients in ordered_item:
            resources[ingredients] -= ordered_item[ingredients]
        print(f"Here is your {selected_drink} ☕.Enjoy!")




def coffee_machine():
    machine_on = True
    while machine_on == True:
        selected_item = input("What would you like? (espresso/latte/cappuccino): ")
        if selected_item == "report":
            print(f"water ={resources['water']}ml")
            print(f"milk ={resources['milk']}ml")
            print(f"coffee= {resources['coffee']}gms")
            print(f"Money =${profit}")

        elif selected_item == "off":
            machine_on = False
        else:
            drink = MENU[selected_item]
            if check_resource(drink['ingredients']) == True:
                print("Please insert coins.")
                total = process_coins()
                if transition_success(drink, total) == True:
                    make_coffee(drink['ingredients'], selected_item)

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {drink['ingredients']}")

coffee_machine()






