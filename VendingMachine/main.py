from FoodDao import *
from Application import application
from MoneyDao import *

#path to csv file with food items
newPath = "vendingmachine.csv"

#creates a new log sheet
newLog = log()

#creates a new vending machine
try:
    newVendingMachine = vendingmachine(newPath)
    application(newVendingMachine, newLog).run()
except:
    print("Something went wrong. The file likely does not exits")
#builds and starts applications


