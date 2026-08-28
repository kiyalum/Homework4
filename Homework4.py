# Task 1


class Product:
    """Represents a product in a store inventory."""

    def __init__(self, name: str, category: str, price: float, product_count: int):
        """Initialize a new Product instance.

        :param name: The name of the product.
        :param category: The category of the product (e.g., 'soft toy', 'construction kit').
        :param price: The price of the product.
        :param product_count: The number of items available in stock.
        """
        self.name = name
        self.category = category
        self.price = price
        self.product_count = product_count

    def update_price(self, new_price: int):
        """Update the price of the product.

        :param new_price: The new price to be set.
        """
        if new_price > 0:
            self.price = new_price
            print(f"The price of {self.name} is now {self.price} UAH.")
        else:
            print("Price must be greater than 0.")

    def update_count(self, amount: int):
        """Update the product stock quantity (positive or negative adjustment).

        :param amount: The number of units to add (positive) or remove (negative).
        """
        if self.product_count + amount >= 0:
            self.product_count += amount
            print(f"New stock quantity for '{self.name}': {self.product_count} units.")
        else:
            print(f"Insufficient stock for '{self.name}'.")

    def __str__(self) -> str:
        """Return a string representation of the product."""
        return (f"\nThe product's name: {self.name} "
                f"\nThe product's category: {self.category}"
                f"\nThe product's price: {self.price}"
                f"\nThe product's count: {self.product_count}")


class Order:
    """Represents a customer's order containing a list of products."""

    def __init__(self):
        """Initialize a new Order instance."""
        self.products_list = []
        self.total_price = self.calculate_total()

    def add_product(self, product: Product, quantity: int):
        """Add a product to the order and recalculate the total amount.

        :param product: The Product object to be added.
        :param quantity: The quantity of the product to be added.
        """
        if product.product_count >= quantity:
            for _ in range(quantity):
                self.products_list.append(product)
            product.update_count(-quantity)
            self.calculate_total()
            print(f"Added {quantity} pieces of '{product.name}' to the order.")
        else:
            print(f"Unable to add '{product.name}': only {product.product_count} left in stock.")

    def calculate_total(self) -> float:
        """Calculate and return the total price of all products in the order.

        :return: Total price of the order.
        """
        self.total_price = sum(product.price for product in self.products_list)
        return self.total_price

    def __str__(self) -> str:
        """Return a string representation of the order."""
        return (f"\nThe order: {len(self.products_list)} items"
                f"\nThe total price: {self.total_price:} UAH")


class Customer:
    """Represents a customer in the system."""

    def __init__(self, name: str, email: str):
        """Initialize a new Customer instance.

        :param name: The name of the customer.
        :param email: The email address of the customer.
        """
        self.name = name
        self.email = email
        self.orders_list = []

    def add_order(self, order: Order):
        """Add a new order to the customer's order history.

        :param order: The order details or order object to be added.
        """
        self.orders_list.append(order)

        print(f"The order has been added to the customer {self.name}.")

    def __str__(self) -> str:
        """Return a string representation of the customer."""
        return (f"\nThe customer's name: {self.name}"
                f"\nThe customer's email: {self.email}"
                f"\nThe customer's total orders: {len(self.orders_list)}")