from pizza import Pizza
from carte_pizzeria import CartePizzeria

"""Test the Pizza class"""


def test_pizza():
    pizza = Pizza("4 fromages", ["Mozzarella", "Chèvre", "Emmental", "Roquefort"], 12.5)
    assert pizza.__str__() == "4 fromages (12.5€) : Mozzarella, Chèvre, Emmental, Roquefort"


"""Test the CartePizzeria class"""


def test_carte_pizzeria():
    carte = CartePizzeria()
    assert carte.is_empty() == True
    assert carte.nb_pizzas() == 0
    pizza = Pizza("4 fromages", ["Mozzarella", "Chèvre", "Emmental", "Roquefort"], 12.5)
    carte.add_pizza(pizza)
    assert carte.is_empty() == False
    assert carte.nb_pizzas() == 1
    carte.remove_pizza(pizza)
    assert carte.is_empty() == True
    assert carte.nb_pizzas() == 0
