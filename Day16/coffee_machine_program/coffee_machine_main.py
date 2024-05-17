from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power_on = True
machine_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while power_on:
    drink_order = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_order == 'off':
        power_on = False
        continue
    else:
        drink = machine_menu.find_drink(drink_order)
        if drink == None:
            print("Resources left in coffee maker:")
            coffee_maker.report()
            continue
        resources_available = coffee_maker.is_resource_sufficient(drink)
        if not resources_available:
            print("Resources left in coffee maker:")
            coffee_maker.report()
            continue
        payment_successful = money_machine.make_payment(drink.cost)
        if not payment_successful:
            print("Resources left in coffee maker:")
            coffee_maker.report()
            continue
        coffee_maker.make_coffee(drink)
        power_on = False

