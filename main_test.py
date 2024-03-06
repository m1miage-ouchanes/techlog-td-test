from pizza import Pizza

def test_pizza():
    pizza = Pizza("4 fromages", ["Mozzarella", "Chèvre", "Emmental", "Roquefort"], 12.5)
    assert pizza.__str__() == "4 fromages (12.5€) : Mozzarella, Chèvre, Emmental, Roquefort"