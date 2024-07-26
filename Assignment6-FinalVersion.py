class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.description = description

    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${item_cost:.2f}")

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        pass

    def modify_item(self, ItemToPurchase):
        pass

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        total_items = self.get_num_items_in_cart()
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {total_items}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.description}")


def print_menu(cart):
    user_input = ''
    menu = """
    MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    """
    
    while user_input != 'q':
        print(menu)
        user_input = input("Choose an option: ")
        if user_input == 'a':
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the quantity: "))
            item_description = input("Enter the item description: ")
            item_to_add = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item_to_add)
        elif user_input == 'r':
            item_name = input("Enter the item name to remove: ")
            cart.remove_item(item_name)
        elif user_input == 'c':
            item_name = input("Enter the item name to modify: ")
            quantity = int(input("Enter the new quantity: "))
            cart.modify_item(item_name, quantity)
        elif user_input == 'i':
            cart.print_descriptions()
        elif user_input == 'o':
            cart.print_total()
        elif user_input == 'q':
            print("Quitting the menu.")
        else:
            print("Invalid option, please try again")


# Main program
cart = ShoppingCart("John Doe", "February 1, 2020")
item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
item2 = ItemToPurchase("Chips", 3, 5, "Semi-sweet")
item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

print_menu(cart)

