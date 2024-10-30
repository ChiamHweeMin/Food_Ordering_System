layout = "{0:<10}{1:<10}{2:<30}"
class Meal:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def get_meal(self):
        print(layout.format("", "=" * 8 , "=" * 30 ))
        lisCnN = list(zip(self.code, self.name))
        dicNnP = dict(list(zip(self.name, self.price)))
        for code, name in lisCnN:
            print(layout.format("", code, name))
        print(layout.format("", "=" * 10, "=" * 30))
        return lisCnN, dicNnP

class Food(Meal):
    def __init__(self, code, name, price):
        Meal.__init__(self, code, name, price)

    def show_food(self):
        print(layout.format("", "=" * 10, "=" * 30))
        print(layout.format("", "-Code-", "-Food-"))
        return Meal.get_meal(self)

class Drink(Meal):
    def __init__(self, code, name, price):
        Meal.__init__(self, code, name, price)

    def show_drink(self):
        print(layout.format("", "=" * 10, "=" * 30))
        print(layout.format("", "-Code-", "-Drink-"))
        return Meal.get_meal(self)