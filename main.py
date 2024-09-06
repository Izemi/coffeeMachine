# Import necessary classes
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of MoneyMachine, CoffeeMaker, and Menu
payment_processor = MoneyMachine()  # Handles payment processing
coffee_machine = CoffeeMaker()  # Manages coffee machine functions like making coffee and reporting resources
drink_menu = Menu()  # Holds the menu and provides information about available drinks

# A variable to control whether the coffee machine is on or off
machine_on = True

# Start the main loop, which continues as long as the coffee machine is "on"
while machine_on:
    # Display available drink options
    available_drinks = drink_menu.get_items()

    # Ask the user for their choice
    user_choice = input(f"What would you like? ({available_drinks}): ")

    # If the user inputs 'off', turn off the coffee machine by exiting the loop
    if user_choice == "off":
        machine_on = False

    # If the user inputs 'report', show the current status of the coffee machine and payment processor
    elif user_choice == "report":
        coffee_machine.report()  # Prints the current resource levels (water, milk, coffee)
        payment_processor.report()  # Prints the current money status

    # If the user selects a valid drink, proceed with the order
    else:
        # Find the drink corresponding to the user's choice
        selected_drink = drink_menu.find_drink(user_choice)

        # Check if there are enough resources to make the drink and if the payment is successful
        if coffee_machine.is_resource_sufficient(selected_drink) and payment_processor.make_payment(
                selected_drink.cost):
            coffee_machine.make_coffee(selected_drink)  # Make the coffee if both checks pass
