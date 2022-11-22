
SIZE_KOEFS = {"min": 0.4, "mid": 0.7, "max": 1}


class Ingredient:
    def __init__(self, name, cost):
        self.name = name
        self.name = cost


class Pizza:
    def __init__(self, name, size, base_cost):
        self.name = name
        self.size = size
        self.base_cost = base_cost

    def __str__(self):
        return f"Pizza {self.name} {self.size}-size {self.base_cost}$"


class DailyPizza(Pizza):
    def __init__(self, name, size, base_cost, day):
        super(DailyPizza, self).__init__(name, size, base_cost)
        self.day = day


class Menu:
    def __init__(self):
        self.pizzas = []
        self.day = []

    def add_pizza_to_menu(self, name, size='mid', base_cost=1, day=0):
        if not (0 < day < 8):
            raise ValueError
        if day not in self.day:
            self.pizzas.append(DailyPizza(name, size, base_cost, day))
            self.day.append(day)
        else:
            self.pizzas[self.day.index(day)] = DailyPizza(name, size, base_cost)

    def find_by_day(self, day:int=1):
        if not (0 < day < 8) and not self.day.index(day):
            raise ValueError

        return self.pizzas[self.day.index(day)]

#
# menu = Menu()
#
# menu.add_pizza_to_menu("pizza1", 'min', 10, 1)
# menu.add_pizza_to_menu("pizza2", 'min', 11, 2)
# menu.add_pizza_to_menu("pizza3", 'min', 12, 3)
# menu.add_pizza_to_menu("pizza4", 'min', 13, 4)
# menu.add_pizza_to_menu("pizza5", 'min', 14, 5)
# menu.add_pizza_to_menu("pizza6", 'min', 15, 6)
# menu.add_pizza_to_menu("pizza7", 'min', 16, 7)
#
#
# week_day = 1
# user_answer = input(f"{menu.find_by_day(week_day)}")