import datetime
from Messages import *
initial_balance = float(0)

'''Log Class'''
class log:
    #initiates a new Log with a starting balance
    def __init__(self):
        self.Balance = initial_balance
 
    #displays the balance that is left on the machine that he user can access
    def display_balance(self):
        print("you have ${:.2f}".format(self.Balance))

    #allows user to input more money
    def feed_money(self):
        #displays balance
        self.display_balance()
        #continues to prompt user for money until money is inserted or the user exits
        while True:
            #this machine only takes $1s, $2s, $5s, and $10s. the machine refueses all other denominations or inputs
            money = input("Please insert $1, $2, $5, $10: $")
            #if the user inputs accepted currency, the balance is updated, and then returns to the main menu
            if money in ('1', '2', '5', '10'):
                #adjusts balance
                self.Balance += float(money)
                #records balance in log: Date FEED MONEY amount_of_money balance_left
                self.log_interaction(f"{datetime.datetime.now()} " + "FEED MONEY: " + 
                                     "${:.2f}".format(float(money)) + " " + "${:.2f}".format(self.Balance))
                return True
            #exits to the main menu
            elif money in ("0", ""):
                return False
            #prompts the uer to input ReAl MoNeY
            else:
                print("Please enter real money or press enter to exit")
    
    #gives back change to the user in $1s, quarters, dimes, and nickles
    def give_change(self):
        change = self.Balance
        coins = [["dollar(s)", 1.00, 0],
            ["quarter(s)", 0.25, 0],
            ["dime(s)", 0.10, 0],
            ["nickle(s)", 0.05, 0]]
        for coin in coins:
            while change >= coin[1]:
                change -= coin[1]
                coin[2] += 1
        for coin in coins:
            print(f"{coin[0]}: {coin[2]}")
        input("Press any key to continue...")
        self.log_interaction(f"{datetime.datetime.now()} " + "GIVE CHANGE: " + 
                             "${:.2f}".format(self.Balance) + " " + "$0.00")
        self.Balance = 0

    def adjust_log_with_food(self, food):
        self.log_interaction(f"{datetime.datetime.now()} " + f"{food.Name} " + "${:.2f}".format(self.Balance) + 
                                 " " + "${:.2f}".format(self.Balance - food.Price))
        self.Balance -= food.Price

    def check_balance_with_food(self, food):
        if self.Balance - food.Price < 0:
            print(f"You do not have enough money. Please insert more money.")
            return False
        return True

    def log_interaction(self, message):
        path = "log.txt"
        file = open("log.txt", "a")
        file.write("\n" + message)
        file.close()


                
