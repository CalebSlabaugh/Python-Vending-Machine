import os
from Messages import *

'''Application Class'''
class application:
    #creates a new application with an inserted vending machine and log
    def __init__(self, vendingMachine, log):
        self.VendingMachine = vendingMachine
        self.Log = log
    
    def run(self):
        #the application displays options onto the screen and deligates user commands to the rest of the classes in the program
        #option 1 displays all of the vending machines food items: location|Name|cost|how many are left
        #option 2 proceeds to the purchase menu (screen 2)
        #option 3 exits application
        print(screen_one_greeting)
        while True:           
            print(screen_one_options)
            selector = input(option_prompt)
            #option 1 selected (displays items)
            if selector == "1":
                self.clear_console()
                self.VendingMachine.print_machine()
                input(continue_prompt) 
            #option 2 selected (proceeds to purchase menu)
            if selector == "2":
                self.screen_two()
            #option 3 selected (exits)
            if selector == "3":
                self.clear_console
                print(thank_you)
                break
            self.clear_console()
     
    def screen_two(self):
        #the application displays options onto the screen and deligates user commands to the rest of the classes in the program
        #option 1 allows the user to input money ($1's, $2's, $5's, $10's)
        #option 2 displays the vending machine items and allows user to purchase an item
        #option 3 exits to first screen
        while True:
            self.clear_console()
            print(screen_two_options)
            self.Log.display_balance()
            selector = input(option_prompt)
            #option 1 (allows user to input money)
            if selector == "1":
                self.clear_console()
                self.Log.feed_money()
            #option 2 (allows user to view and purchase items)
            if selector == "2":
                self.clear_console()
                self.buy_food()
            #option 3 (exits to main menu/screen 1)
            if selector == "3":
                self.clear_console()
                self.Log.give_change()
                break

    

    def buy_food(self):
        #displays food items and balance in vending machine
        self.VendingMachine.print_machine()
        self.Log.display_balance()
        #selects food from designated location
        foodSelected = input(please_select)
        #checks to see if the location inputed matches any of the food items locations
        for item in self.VendingMachine.stock:
            if foodSelected.upper() == item.Location:
                #checks to see if the user has enough money
                if self.Log.check_balance_with_food(item):
                    #dispenses food and updates balance (if not sold out)
                    if self.VendingMachine.dispense_food(item):
                        self.Log.adjust_log_with_food(item)
                input(continue_prompt)
                break

    #clears screen
    def clear_console(self):
        os.system('cls')