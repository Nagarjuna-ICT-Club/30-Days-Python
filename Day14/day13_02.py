class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "*Animal Sound*"


class Cat(Animal):
    # super() is used to access methods and properties
    # from the superclass.
    def __init__(self, name, lifespan):
        super().__init__(name)
        self.lifespan = lifespan    # Add a `lifespan` property

    def speak(self):
        return "meow"


cat = Cat("ichi", 15)

print(cat.speak())
