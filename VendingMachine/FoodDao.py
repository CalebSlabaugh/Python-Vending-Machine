from Classes.Candy import candy
from Classes.Chips import chip
from Classes.Gum import gum
from Classes.Drink import drink
import csv
#this class deals with food items

class vendingmachine:
    def __init__(self, path):
        #reads all of the items in the csv file and loads them into a list of Food items
        try:
            file = open(path)
            csvreader = csv.reader(file)
            self.stock = []
            for row in csvreader:
                className = row[-1].lower()
                constructor = globals()[className]
                location = row[0]
                name = row[1]
                price = row[2]
                instance = constructor(location, name, price)
                self.stock.append(instance)
            file.close
        except:
            raise

    def print_machine(self):
        #Prints the Food items in the stock list: location|Name|cost|how many are left
        for item in self.stock:
            print(f"{item.Location}|{item.Name}|" + "${:.2f}".format(item.Price) + f"|Left: {item.Left}")
        #food = candy()

    def dispense_food(self, food):
        #dispenses food and updates their stock (subtracts one from Left)
        return food.print_item()
        


