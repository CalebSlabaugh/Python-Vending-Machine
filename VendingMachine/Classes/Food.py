from abc import ABC, abstractmethod

beginning_amount_of_items = 5

'''Abstract Food Class '''
class food(ABC):
    #constructs a food item
    def __init__(self,location: str, name: str, price: str):
        self.Name = name
        self.Price = float(price)
        self.Location = location
        self.Left = beginning_amount_of_items
    
    #updates food items left
    def update_food_number(self):
        if self.Left > 0:
            --self.Left
            return True
        else:
            return False

    #implements a method where item prints its message
    @abstractmethod
    def print_item(self):
        pass

    #food.__doc__ = "abstract class takes strings that determine the name, price, and location of the food item"


