GREETING = "Welcome to our pizzeria!\nToday we have pizza of the day - "


class Order:
    def __init__(self, pizza, total_cost, list_ing):
        self.pizza = pizza
        self.total_cost = total_cost
        self.toppings = list_ing

    def __str__(self):
        res = f"You ordered:\n{self.pizza}\n Additional:\n"
        for i in self.toppings:
            res += f"{i}\n"
        return res + f"Total cost: {self.total_cost}$"


class Ingredient:
    def __init__(self, name, cost, represent):
        self.name = name
        self.represent = represent
        self.cost = cost

    def __str__(self):
        return f"{self.name} - {self.cost}$"


class Pizza:
    def __init__(self, name, base_cost):
        self.name = name
        self.base_cost = base_cost

    def __str__(self):
        return f"{self.name} cost: {self.base_cost}$"


class DailyPizza(Pizza):
    def __init__(self, name, base_cost, day):
        super(DailyPizza, self).__init__(name, base_cost)
        self.day = day


class Menu:
    def __init__(self):
        self.pizzas = []
        self.day = []
        self.ingredients = []
        self.ingredients_repr = []
        self.orders = []

        self.fill_menu()

    def add_pizza_to_menu(self, name, base_cost, day):
        if not (0 < day < 8):
            raise ValueError
        if day not in self.day:
            self.pizzas.append(DailyPizza(name, base_cost, day))
            self.day.append(day)
        else:
            self.pizzas[self.day.index(day)] = DailyPizza(name, base_cost, day)

    def find_pizza_by_day(self, day):
        if not (0 < day < 8) and not self.day.index(day):
            raise ValueError
        return self.pizzas[self.day.index(day)]

    def add_ingredient_to_menu(self, name, cost, ingredients_repr):
        if ingredients_repr not in self.ingredients_repr:
            self.ingredients.append(Ingredient(name, cost, ingredients_repr))
            self.ingredients_repr.append(ingredients_repr)
        else:
            self.ingredients[self.ingredients_repr.index(ingredients_repr)] = Ingredient(name, cost, ingredients_repr)

    def find_ingredient(self, ingredients_repr):
        if ingredients_repr not in self.ingredients_repr:
            raise ValueError
        return self.ingredients[self.ingredients_repr.index(ingredients_repr)]

    def fill_menu(self):
        # name, cost, representation
        self.add_ingredient_to_menu("Pepperoni", 2, "p")
        self.add_ingredient_to_menu("Sausage", 3, "s")
        self.add_ingredient_to_menu("Mushrooms", 2, "m")
        self.add_ingredient_to_menu("Bacon", 3, "b")
        self.add_ingredient_to_menu("Onions", 1, "o")
        self.add_ingredient_to_menu("Extra Cheese", 1, "e")
        self.add_ingredient_to_menu("Chicken", 3, "c")

        # name, cost, week day
        self.add_pizza_to_menu("Cheese Pizza", 10, 1)
        self.add_pizza_to_menu("Veggie Pizza", 11, 2)
        self.add_pizza_to_menu("Pepperoni Pizza", 12, 3)
        self.add_pizza_to_menu("Meat Pizza", 13, 4)
        self.add_pizza_to_menu("Margherita Pizza", 14, 5)
        self.add_pizza_to_menu("BBQ Chicken Pizza", 15, 6)
        self.add_pizza_to_menu("Hawaiian Pizza", 16, 7)

    def make_order(self, week_day):
        __pizza_of_day = self.find_pizza_by_day(week_day)
        __total_cost = __pizza_of_day.base_cost
        __tmp_ingredient = None
        __list_of_ingredients = []
        print(f"{GREETING}{__pizza_of_day}")

        order_not_done = True
        while order_not_done:
            print("Do you wont additional toppings?\nChoose from below:")
            for ingredient in self.ingredients:
                print(f"{ingredient} (press {ingredient.represent} to choose)")
            user_answer = input("Type letter or press ENTER to finish\n")
            if user_answer == "":
                order_not_done = False
            else:
                __tmp_ingredient = self.find_ingredient(user_answer)
                __list_of_ingredients.append(__tmp_ingredient)
                __total_cost += __tmp_ingredient.cost
                print(f"{self.find_ingredient(user_answer)} added\nTotal cost:{__total_cost}")

        order = Order(__pizza_of_day, __total_cost, __list_of_ingredients)
        self.orders.append(order)
        print(order)
