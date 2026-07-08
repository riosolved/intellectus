
class Item:
    name: str
    weight: float
    value: float

    def __init__(self, **keyword_arguments):
        self.name = keyword_arguments.get("name")
        self.weight = keyword_arguments.get("weight")
        self.value = keyword_arguments.get("value")


class Inventory:
    items: dict[str, list[Item]] = {}

    def remove(self, item: Item):
        del self.items[item.name]

    def add(self, item: Item):
        name = item.name

        if name not in self.items:
            self.items[name] = []

        self.items[name].append(item)

class Store:
    budget: float
    inventory = Inventory()
    cart: list[Item] = []

    items = {
        "apple": Item(name="apple", weight=0.2, value=1),
        "orange": Item(name="orange", weight=0.3, value=1.5),
        "milk": Item(name="milk", weight=1.0, value=3)
    }

    def __init__(self, budget: float):
        self.budget = budget

        self.inventory.add(self.items["apple"])
        self.inventory.add(self.items["orange"])
        self.inventory.add(self.items["milk"])

    def buy(self, item: Item):
        if self.budget < item.value:
            raise Exception("Not enough money to buy " + item.name)

        self.budget -= item.value

        if item.name in self.inventory.items:
            self.cart.append(item)
            self.inventory.remove(item)
        else:
            print("Item " + item.name + " is not available in the store")


def main():
    store = Store(
        budget=100
    )

    store.buy(store.items["apple"])
    store.buy(store.items["apple"])

    assert len(store.cart) == 2, "There should be 2 apples in the shopping bag" + " but there are " + str(len(store.cart))

# Execute the main program
main()