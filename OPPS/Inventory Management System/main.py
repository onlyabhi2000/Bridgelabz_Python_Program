class Product:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}"

    def __repr__(self):
        return f"Product(name='{self.name}', category='{self.category}')"


class Inventory:
    def __init__(self):
        self.cart = []

    def add_items(self, product, quantity, price):
        for item in self.cart:
            if item['name'] == product.name:
                item['quantity'] += quantity
                return
        self.cart.append({
            'name': product.name,
            'category': product.category,
            'quantity': quantity,
            'price': price
        })

    def remove_items(self, product, quantity):
        for item in self.cart:
            if item['name'] == product.name:
                if quantity >= item['quantity']:
                    self.cart.remove(item)
                    print(f"Removed all '{product.name}'")
                else:
                    item['quantity'] -= quantity
                    print(f"Removed thgee{quantity} '{product.name}' from inventory.")
                return
        print(f"item named '{product.name}' doesnt exist in theinventory.")

    def update_price(self, product, new_price):
        for item in self.cart:
            if item['name'] == product.name:
                item['price'] = new_price
                print(f"Updated price of '{product.name}' is {new_price}")
                return
        print(f"Item '{product.name}' not found to update price.")

    def get_total_value(self):
        total = 0
        for item in self.cart:
            total += item['quantity'] * item['price']
        return total

    def show_inventory(self):
        if not self.cart:
            print("Inventory is empty.")
        else:
            for item in self.cart:
                print(f"{item['name']} ({item['category']}): {item['quantity']} {item['price']}")
            print(f"Total Inventory Value:{self.get_total_value()}")


p1 = Product("Pen", "Stationery")
p2 = Product("Soap", "Toiletries")
p3 = Product("Notebook", "Stationery")

inv = Inventory()
inv.add_items(p1, 10, 5)
inv.add_items(p2, 4, 20)
# inv.add_items(p1, 5, 5) 
inv.add_items(p3, 2, 30)

inv.show_inventory()

inv.remove_items(p2, 2)
inv.update_price(p1, 6)

inv.show_inventory()
