# salty_walrus.py — Code Review Notes

A reference review of the inventory/store exercise. Organized from
"will crash" down to "style." The recurring theme is **shared mutable
class attributes** — it showed up in three places.

---

## 🔴 Blocking bugs (program can't run correctly)

**1. `logging` not imported**
Add `import logging` at the top. In Python, almost everything outside the
built-ins must be explicitly imported before use (unlike JS `console`).

**2. `store.cart` doesn't exist**
`Store` has `self.inventory`, never a `cart`. Referencing `store.cart`
raises `AttributeError`.

**3. `shopping_bag` doesn't exist**
Leftover name from an earlier version — nothing defines it in `main`.
Raises `NameError`.

**4. The assert contradicts what `buy` does**
`buy` *removes* apples from the store's inventory, then the assert expects
2 apples to exist somewhere. Buying and counting fight each other because
there's no "cart" that purchases go into.

---

## 🟠 Logic bugs (runs, but wrong behavior)

**5. `remove` deletes the entire entry, not one item**
```python
def remove(self, item):
    del self.items[item.name]     # wipes ALL apples at once
```
First `buy(apple)` removes every apple; the second finds none. Buying one
should reduce the count by one.

**6. `buy` charges before checking availability**
```python
self.budget -= item.value              # money taken first
if item.name in self.inventory.items:  # availability checked after
    ...
else:
    logging.error(...)                 # ...but you already paid!
```
Check availability FIRST, then deduct.

**7. Shared mutable class attributes (the big one)**
```python
class Inventory:
    items: dict[...] = {}      # one dict shared by EVERY Inventory

class Store:
    inventory = Inventory()    # one inventory shared by EVERY Store
    items = { ... }            # same problem
```
Anything mutable defined at class level is shared across ALL instances.
Two stores would stomp on each other. These belong in `__init__` as
`self.items = {}`, `self.inventory = Inventory()`, etc.

**==> The #1 habit to internalize: never put mutable state ({}, [], or an
object) at class level. Put it in __init__ so each instance owns its own.==**

---

## 🟡 Design / idiom

**8. `**keyword_arguments` on `Item` is over-engineered**
```python
def __init__(self, **keyword_arguments):
    self.name = keyword_arguments.get("name")
```
`name`, `weight`, `value` are required and known. Spell them out — it's
clearer AND safer. `.get()` silently returns `None` on a typo, so
`Item(nmae="apple")` gives a nameless item with no error. Prefer:
```python
def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
```
`**kwargs` is the WRONG tool when you have a fixed, known set of fields.

**9. The triple-quoted block in `add`**
That string sitting mid-method as fake commented-out code is harmless but
still gets evaluated at runtime. Delete it, or use `#` for real comments.

**10. `raise Exception(...)`**
Works, but `Exception` is the most generic type — callers can't catch just
this case. Prefer a named error: `raise ValueError("Not enough money...")`.

---

## The deeper issue: what does "buy" mean?

The model was missing a piece: nowhere for bought items to GO. Natural model:

- **Store** has an inventory (what's for sale).
- **buying** moves one item from the store's inventory into the
  **customer's** inventory (a cart/bag).
- Then you assert the CART has 2 apples — which lines up with `buy` being
  called twice.

---

## Consistent reference version

```python
import logging


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


class Slot:                       # "this item, this many"
    def __init__(self, item):
        self.item = item
        self.count = 1


class Inventory:
    def __init__(self):
        self.items = {}           # name -> Slot

    def add(self, item):
        if item.name in self.items:
            self.items[item.name].count += 1
        else:
            self.items[item.name] = Slot(item)

    def remove(self, item):
        if item.name not in self.items:
            raise KeyError(item.name + " not in inventory")
        self.items[item.name].count -= 1
        if self.items[item.name].count == 0:
            del self.items[item.name]


class Store:
    def __init__(self, budget):
        self.budget = budget
        self.inventory = Inventory()
        self.catalog = {
            "apple": Item(name="apple", weight=0.2, value=1),
            "orange": Item(name="orange", weight=0.3, value=1.5),
            "milk": Item(name="milk", weight=1.0, value=3),
        }
        for item in self.catalog.values():
            self.inventory.add(item)

    def buy(self, item, cart):
        if item.name not in self.inventory.items:
            logging.error("Item %s is not available", item.name)
            return
        if self.budget < item.value:
            raise ValueError("Not enough money to buy " + item.name)

        self.budget -= item.value
        self.inventory.remove(item)   # leaves the store
        cart.add(item)                # enters the cart


def main():
    store = Store(budget=100)
    cart = Inventory()

    store.buy(store.catalog["apple"], cart)
    store.buy(store.catalog["apple"], cart)

    assert cart.items["apple"].count == 2, "There should be 2 apples in the cart"
    print("2 apples in the cart.")


main()
```

Once the model is right, everything lines up: buy twice -> cart count is 2
-> assert passes -> budget dropped by 2, store's apple stock dropped by 2.
No contradictions.

---

## Quick reference: concepts that came up

| Concept        | Key point                                                        |
|----------------|------------------------------------------------------------------|
| `__init__`     | The constructor — runs when you create an object. Sets up data.  |
| `self`         | "This particular object." Always the first method parameter.     |
| named args     | `Item(name="apple")` — order-independent, clearer than position. |
| default args   | `def __init__(self, age=1)` — makes a parameter optional.        |
| `**kwargs`     | Catch leftover NAMED args as a dict. Use only for open-ended input. |
| `*args`        | Catch leftover POSITIONAL args as a tuple.                       |
| KeyError       | Reading a missing dict key is an ERROR in Python (not `undefined`). |
| no spread      | JS `{...obj}` has no object equivalent; `{**dict}` works for dicts only. |
| class-level    | Mutable class attributes are SHARED across instances. Use `__init__`. |
```
