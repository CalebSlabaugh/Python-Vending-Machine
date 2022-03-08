from Classes.Food import food

class candy(food):
    def __init__(self, name, price, location):
        super().__init__(name, price, location)

    def print_item(self):
        if self.Left < 1:
            print("Sorry, sold out")
            return False
        print("Munch Munch, Yum!")
        self.Left -= 1
        return True


