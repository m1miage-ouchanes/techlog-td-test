from pizza import Pizza


class CartePizzeria:
    def __init__(self):
        self.__pizzas: list = []

    def is_empty(self) -> bool:
        return len(self.__pizzas) == 0

    def nb_pizzas(self) -> int:
        return len(self.__pizzas)

    def add_pizza(self, pizza: Pizza) -> None:
        self.__pizzas.append(pizza)

    def remove_pizza(self, pizza: Pizza) -> None:
        self.__pizzas.remove(pizza)
