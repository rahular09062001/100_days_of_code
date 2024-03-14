
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def cm_resource():
    global resources
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${resources['money']}")


def cm_coins(x):
    global MENU
    global resources
    global total
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickles = int(input("How many nickles : "))
    pennies = int(input("How many pennies : "))
    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    if(total >= MENU[x]['cost']):
        resources['money'] = resources['money'] + MENU[x]['cost']
        return True
    else:
        return False

def cm_coin_return(x):
    global MENU
    global total
    return total - MENU[x]['cost']


def cm_resource_check(x):
    global MENU
    check_list = []
    for i in MENU[x]["ingredients"]:
        check_list.append(int(1))
    j=0
    for i in MENU[x]["ingredients"]:
        if(resources[i] < MENU[x]['ingredients'][i]):
            check_list[j]=int(0)
        j=j+1
    if(int(0) in check_list):
        return False
    else:
        return True

def cm_disp_res(x):
    global MENU
    global check_res
    check_res = []
    for i in MENU[x]['ingredients']:
        if(resources[i] < MENU[x]['ingredients'][i]):
            check_res.append(i)

def cm(x):
    global MENU
    global resources
    for i in MENU[x]['ingredients']:
        resources[i] = resources[i] - MENU[x]['ingredients'][i]
    print(f'Here is your {x} ☕, Enjoy !....')

def cm_total_fn(x):
    if (cm_resource_check(x)):
        if (cm_coins(x)):
            print(f" Here is ${cm_coin_return(x)}dollars in change.")
            cm(x)
        else:
            print(f"Sorry that's not enough money. Money refunded.")
            print(f'Coin return : ${total}')
    else:
        cm_disp_res(x)
        for i in check_res:
            print(f'There is not enough {i}')

cm_condition = True

while (cm_condition):
    cm_inp = input("What would you like ? (espresso/latte/cappuccino)  : ").lower()

    if (cm_inp=='report'):
        cm_resource()

    elif(cm_inp=='espresso'):
        cm_total_fn(cm_inp)

    elif (cm_inp == 'latte'):
        cm_total_fn(cm_inp)

    elif (cm_inp == 'cappuccino'):
        cm_total_fn(cm_inp)

    elif (cm_inp == 'off'):
        cm_condition = False

