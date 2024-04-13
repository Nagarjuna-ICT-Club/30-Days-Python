class Drink:
    def __init__(self, name):
        self.name = name

    def taste(self):
        pass


class Coffee(Drink):
    def __init__(self, name, syrup_amt):
        super().__init__(name)
        self.syrup_amt = syrup_amt

    def taste(self):
        if self.syrup_amt > 3:
            return "sweet"
        return "bitter"


class Tea(Drink):
    def __init__(self, name, sugar_cube_amt):
        super().__init__(name)
        self.sugar_cube_amt = sugar_cube_amt

    def taste(self):
        if self.sugar_cube_amt > 0:
            return "sweet"
        return "kinda bitter"


coffee = Coffee("Cappuccino", 2)
print(coffee.taste())

tea = Tea("Milk Tea", 3)
print(tea.taste())
