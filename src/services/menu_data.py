import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self._data = {}

        with open(source_path, "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                dish_ingredients = row["ingredient"]
                dish_recipe_amount = int(row["recipe_amount"])

                if dish_name not in self._data:
                    dish = Dish(dish_name, dish_price)
                    dish.add_ingredient_dependency(
                        Ingredient(dish_ingredients), dish_recipe_amount
                    )

                    self._data[dish_name] = dish
                else:
                    self._data[dish_name].add_ingredient_dependency(
                        Ingredient(dish_ingredients), dish_recipe_amount
                    )

    def __eq__(self, __value: object) -> bool:
        return self.__repr__() == __value.__repr__()

    @property
    def dishes(self):
        return set(self._data.values())
