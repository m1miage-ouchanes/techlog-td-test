class Pizza:

    def __init__(self, nom, ingredients, prix):
        self.__nom: str = nom
        self.__ingredients: list = ingredients
        self.__prix: float = prix

    def __str__(self):
        return f"{self.__nom} ({self.__prix}€) : {', '.join(self.__ingredients)}"
