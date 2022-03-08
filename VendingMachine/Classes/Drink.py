from Classes.Food import food

class drink(food):
    def __init__(self, name, price, location):
        super().__init__(name, price, location)

    def print_item(self):
        if self.Left == 0:
            print("Sorry, sold out")
            return False
        print("Glug Glug, Yum!")
        self.Left -= 1
        return True


