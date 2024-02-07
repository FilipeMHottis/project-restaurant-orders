from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


def test_ingredient():
    # Teste: A classe pode ser instanciada
    # corretamente de acordo com a assinatura esperada
    ingredient = Ingredient("queijo mussarela")
    assert isinstance(ingredient, Ingredient)

    # Teste: O atributo conjunto restrictions é populado como esperado
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions
    assert ingredient.name == "queijo mussarela"

    # Teste: O método mágico __repr__ funciona como esperado
    expected_repr = "Ingredient('queijo mussarela')"
    assert repr(ingredient) == expected_repr

    # Teste: O método mágico __eq__ funciona como esperado
    other_ingredient = Ingredient("queijo mussarela")
    assert ingredient == other_ingredient

    # Teste: O método mágico __hash__ funciona como esperado
    assert hash(ingredient) == hash(other_ingredient)
    assert hash(ingredient) == hash("queijo mussarela")
