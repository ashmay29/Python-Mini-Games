from data import MENU
from data import resources

total_money = 0
is_machine_on  = True

while is_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        is_machine_on = False
    elif order =="edit menu":
        print("What item would you like to add on the menu:")

    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g \n")
        print(f"The total money cashed in the machine is ${total_money}.")

    elif order == "refill":
        water = int((input("Enter the amount of water you wish to add:")))
        milk = int((input("Enter the amount of milk you wish to add:")))
        coffee = int((input("Enter the amount of coffee you wish to add:")))
        resources['water'] += water
        resources['milk'] += milk
        resources['coffee'] += coffee
        
    elif order in MENU:
        if resources["water"] >= MENU[order]["ingredients"]["water"]  and resources["milk"] >= MENU[order]["ingredients"]["milk"] and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            resources["water"] -= MENU[order]["ingredients"]["water"]
            resources["milk"] -= MENU[order]["ingredients"]["milk"]
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
            print(f"Here is your order. Enjoy! That would be ${MENU[order]['cost']}")
            quarters = int(input("Insert the quarters:"))
            dimes = int(input("Insert the dimes:"))          
            nickles = int(input("Insert the nickles:"))            
            pennies = int(input("Insert the pennies:"))            
            cost = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
            if cost > MENU[order]["cost"]:
                change = cost - MENU[order]["cost"]
                new_cost = cost-change
                print(f"Here is your change: ${change:.2f}")
                total_money += new_cost
            elif cost == MENU[order]["cost"]:
                total_money += cost
            else:
                print("Sorry, that's not enough money. Money refunded.")
        elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
    else:
        print(f"Sorry we do not serve {order}.")