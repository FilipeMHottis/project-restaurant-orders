from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    # Teste: A classe pode ser instanciada corretamente
    class_instance = Dish("Lasanha", 50.0)
    assert isinstance(class_instance, Dish)

    # Teste: Os métodos da classe funcionam como esperado
    assert class_instance.name == "Lasanha"
    assert class_instance.price == 50.0
    assert class_instance.recipe == {}

    class_instance.add_ingredient_dependency(Ingredient("massa de lasanha"), 1)
    class_instance.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    class_instance.add_ingredient_dependency(Ingredient("presunto"), 1)

    assert class_instance.recipe == {
        Ingredient("massa de lasanha"): 1,
        Ingredient("queijo mussarela"): 1,
        Ingredient("presunto"): 1,
    }

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert class_instance.get_restrictions() == expected_restrictions

    # Teste: São levantados erros ao criar pratos inválidos;
    with pytest.raises(TypeError):
        Dish("Lasanha", "50.0")

    with pytest.raises(ValueError):
        Dish("Lasanha", -50.0)

        # Teste: Verificação de igualdade (Diferentes)
    other_dish = Dish("Pizza", 30.0)
    assert class_instance != other_dish

    # Teste: Verificação de igualdade (Iguais)
    same_dish = Dish("Lasanha", 50.0)
    assert class_instance == same_dish

    # Teste: get_ingredients()
    ingredients_set = class_instance.get_ingredients()
    expected_ingredients_set = {
        Ingredient("massa de lasanha"),
        Ingredient("queijo mussarela"),
        Ingredient("presunto"),
    }
    assert ingredients_set == expected_ingredients_set

    # Teste: __hash__ (Diferentes)
    assert hash(class_instance) != hash(other_dish)

    # Teste: __hash__ (Iguais)
    assert hash(class_instance) == hash(same_dish)

    # Teste: __repr__ (String representativa)
    expected_repr = f"Dish('Lasanha', R${class_instance.price:.2f})"
    assert repr(class_instance) == expected_repr
