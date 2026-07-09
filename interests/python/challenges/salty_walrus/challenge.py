"""
STORY
A salty walrus runs a small seafood market and keeps track of inventory using a dictionary. Each item has a name, a price per unit, and a quantity in stock. The walrus wants to compute the total value of the inventory, but also needs to enforce rules: items must have positive prices and quantities, and the walrus can only process up to 100 units of any single item.

YOUR TASK
1. Define a function `calculate_inventory_value(inventory)` that:
   - Takes a dictionary `inventory` where keys are item names (strings) and values are dictionaries with keys 'price' and 'quantity'.
   - Returns the total value of all items in inventory, computed as sum of (price * quantity) for each item.
   - Raises a ValueError if any item has a negative price or quantity.
   - Raises a ValueError if any item has a quantity greater than 100.

2. Define a function `add_item(inventory, name, price, quantity)` that:
   - Takes an existing inventory dictionary and adds a new item with given name, price, and quantity.
   - Updates the inventory dictionary in place.
   - Raises a ValueError if price or quantity is negative.
   - Raises a ValueError if quantity exceeds 100.

ASSERTS
inventory = {
    "salmon": {"price": 5.0, "quantity": 20},
    "shrimp": {"price": 8.0, "quantity": 15},
    "cod": {"price": 3.0, "quantity": 40}
}
assert calculate_inventory_value(inventory) == 290.0

inventory["tuna"] = {"price": 12.0, "quantity": 5}
assert calculate_inventory_value(inventory) == 350.0

add_item(inventory, "mackerel", 6.0, 25)
assert calculate_inventory_value(inventory) == 490.0

# Test error handling
try:
    add_item(inventory, "invalid", -1.0, 10)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

try:
    add_item(inventory, "invalid", 5.0, 150)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

BACKGROUND
Dictionaries in Python store data as key-value pairs. For example, `{"a": 1, "b": 2}` has two keys ("a" and "b") with corresponding values (1 and 2). You can access a value by its key using square brackets: `dict["a"]` returns 1.

When iterating over a dictionary, you get the keys. To access both keys and values, use `.items()`, which gives pairs like `("a", 1)`.

A loop over a dictionary's keys looks like:
```python
for key in dict:
    print(key)
```

To loop over both keys and values:
```python
for key, value in dict.items():
    print(key, value)
```

The `ValueError` is a built-in Python exception used to signal invalid input. You raise it with `raise ValueError("message")`.

Mathematically, the total inventory value is the sum of (price × quantity) for all items.

Python does not allow negative numbers in dictionary keys or values directly, but you must check and enforce constraints yourself.

In Python, when a key doesn't exist in a dictionary, accessing it with `dict[key]` raises a `KeyError`. Using `.get(key, default)` avoids this by returning the default value instead.

HINTS
1. You can loop over items in a dictionary using `.items()`.
2. The function `calculate_inventory_value` must compute and sum price * quantity for each item.
3. Both functions need to validate that inputs are non-negative and quantities do not exceed 100.
4. Use `raise ValueError("message")` to signal invalid input conditions.
"""