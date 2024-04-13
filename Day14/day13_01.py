class Animal:
    def __init__(self, name):
        self.name = name

    def pat(self):
        pass


class Cat(Animal):
    # Inherits all the atrributes and methods from the Parent(Animal) Class

    # Override the parent `pat` method
    def pat(self):
        return "Meow"


cat = Cat("neko")

print(cat.pat())
