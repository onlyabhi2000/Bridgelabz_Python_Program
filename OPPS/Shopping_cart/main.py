class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name, quantity):
        if item_name in self.cart:
            if self.cart[item_name]['quantity'] <= quantity:
                del self.cart[item_name]
            else:
                self.cart[item_name]['quantity'] -= quantity

    def calculate_total(self):
        total = 0
        for item in self.cart.values():
            total += item['quantity'] * item['price']
        return total

    def show_cart(self):
        for key, value in self.cart.items():
            print(key, value)



cart1 = ShoppingCart()
cart1.add_item('egg', 5, 20)

# cart1.remove_item('egg', 2)


cart1.show_cart()


print("Total:", cart1.calculate_total())
