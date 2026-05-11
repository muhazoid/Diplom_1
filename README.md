## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие класс `Burger`:

- `test_set_buns_burger_bun_assigned` — проверка, что булочка устанавливается корректно
- `test_add_ingredient_burger_ingredient_added_to_list` — проверка добавления ингредиента в список
- `test_remove_ingredient_burger_ingredient_removed_from_list` — проверка удаления ингредиента по индексу
- `test_remove_ingredient_burger_last_element_removed` — проверка удаления последнего элемента
- `test_move_ingredient_burger_order_changed` — проверка изменения порядка ингредиентов
- `test_move_ingredient_burger_same_position_unchanged` — проверка перемещения на ту же позицию
- `test_get_price_burger_correct_price_returned` — проверка расчёта цены (параметризован)
- `test_get_price_burger_without_bun_error_raised` — проверка ошибки при отсутствии булочки
- `test_get_receipt_burger_receipt_contains_bun_and_ingredients` — проверка чека с булочкой и ингредиентом
- `test_get_receipt_burger_receipt_without_ingredients_correct` — проверка чека без ингредиентов
- `test_get_receipt_burger_different_ingredient_types_in_receipt` — проверка разных типов ингредиентов в чеке (параметризован)
- `test_burger_init_burger_default_state_correct` — проверка начального состояния бургера

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` — пакет, содержащий код программы: классы `Bun`, `Burger`, `Ingredient`, `Database`
- `tests` — пакет, содержащий тесты. Например, `test_burger.py`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

> `$ pytest --cov=praktikum --cov-report=html`