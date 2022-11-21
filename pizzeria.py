
SIZE_KOEFS = {"min": 0.4, "mid": 0.7, "max": 1}


class Ingredient:
    def __init__(self, name, cost):
        self.name = name
        self.name = cost


class Pizza:
    def __init__(self, name, size, base_ingredients, add_toppings):
        self.name = name
        self.size = size
        self.base_ingredients = []
        self.added_toppings = []


class Menu:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self):
        pass

