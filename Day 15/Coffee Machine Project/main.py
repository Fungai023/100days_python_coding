import Coffee_Machine_Data as data

amount = 0

def user_order() :
     choice = input("What would like? (espresso/latte/cappuccino) : ")
     order_complete = False
     prompts = ['espresso','latte' , 'cappuccino','off','report']
     while not choice.isalpha() or order_complete:
         choice = input("What would like? (espresso/latte/cappuccino) : ")
     if choice.lower() == "off" :
         print("Program should end")

def print_report(updated_resources):
    for item in updated_resources:
        print(item + " :  " + updated_resources[item])
    print("Amount :  $" + str(amount))

def check_resources(updated_resources, choice):
    coffee_type = data.MENU.get(choice)
    for item in coffee_type.values():
        for i in updated_resources.values():
            if item == i and coffee_type[item]> updated_resources[i]:
                insufficient = f'  {item}'
    print(f"Sorry there is not enough {insufficient}")


def process_coins():
    return ""

def check_transaction_successful():
    return ""

def make_coffee(choice, cost):
    global amount
    updated_ingredients = data.resources.copy()
    menu = data.MENU
    for coffee_type in menu.items():
        if choice == coffee_type:
            reducing_ingredients(coffee_type , updated_ingredients)
            amount += cost


def reducing_ingredients(coffee_type, resources):
    for item in coffee_type.values():
        for i in resources.values():
            if item == i :
                result = i - item
                resources[i] = result
    return resources



# if __name__ = "__main__":
#     main()