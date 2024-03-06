class CartePizzeriaException(Exception):
    def __init__(self, message="Erreur dans la carte des pizzas"):
        self.__message = message
        super().__init__(self.__message)

    def __str__(self):
        return f"{self.__message}"

