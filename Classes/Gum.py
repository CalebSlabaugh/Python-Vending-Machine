from Classes.Food import food

class gum(food):
    def __init__(self, name, price, location):
        super().__init__(name, price, location)

    def print_item(self):
        if self.Left == 0:
            print("Sorry, sold out")
            return False
        print("Chew Chew, Yum!")
        self.Left -= 1
        return True


