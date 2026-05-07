import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_burger_bun_assigned(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_burger_ingredient_added_to_list(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient_burger_ingredient_removed_from_list(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert ingredient1 not in burger.ingredients
        assert ingredient2 in burger.ingredients

    def test_remove_ingredient_burger_last_element_removed(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(1)

        assert ingredient1 in burger.ingredients
        assert ingredient2 not in burger.ingredients

    def test_move_ingredient_burger_order_changed(self):
        burger = Burger()
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    def test_move_ingredient_burger_same_position_unchanged(self):
        burger = Burger()
        ing1, ing2 = Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(1, 1)

        assert burger.ingredients == [ing1, ing2]

    @pytest.mark.parametrize("bun_price, ing_prices, expected", [
        (100, [50, 50], 300),
        (200, [], 400),
        (150, [100], 400),
        (0, [0, 0, 0], 0),
    ])
    def test_get_price_burger_correct_price_returned(self, bun_price, ing_prices, expected):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ing_prices:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)

        assert burger.get_price() == expected

    def test_get_price_burger_without_bun_error_raised(self):
        burger = Burger()
        
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_burger_receipt_contains_bun_and_ingredients(self):
        burger = Burger()
        
        bun = Mock()
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient.get_name.return_value = "Ketchup"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== Test Bun ====)\n"
            "= sauce Ketchup =\n"
            "(==== Test Bun ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert receipt == expected_receipt

    def test_get_receipt_burger_receipt_without_ingredients_correct(self):
        burger = Burger()
        
        bun = Mock()
        bun.get_name.return_value = "Plain Bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== Plain Bun ====)\n"
            "(==== Plain Bun ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert receipt == expected_receipt

    @pytest.mark.parametrize("ingredient_type, type_display", [
        (INGREDIENT_TYPE_SAUCE, "sauce"),
        (INGREDIENT_TYPE_FILLING, "filling"),
    ])
    def test_get_receipt_burger_different_ingredient_types_in_receipt(self, ingredient_type, type_display):
        burger = Burger()
        
        bun = Mock()
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = "Test Ingredient"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        assert f"= {type_display} Test Ingredient =" in receipt

    def test_burger_init_burger_default_state_correct(self):
        burger = Burger()
        
        assert burger.bun is None
        assert burger.ingredients == []