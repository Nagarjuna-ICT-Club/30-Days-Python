# class
class Mobile:
    # __init__() automatically executes when an object is created
    # 'self' is a reference to the current instance
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # method
    def increase_price(self, percent):
        self.price += percent/100 * self.price


# object
mob = Mobile('apple', 'Xr', 1200)


mob.increase_price(20)
print(mob.price)
