# Task 1


class Product:
    """Represents a product in a store inventory."""

    def __init__(self, name: str, category: str, price: int | float, product_count: int):
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

    def update_price(self, new_price: int) -> None:
        """Update the price of the product.

        :param new_price: The new price to be set.
        """
        if new_price < 0:
            raise ValueError("New price cannot be negative.")

        self.price = new_price

        print(f"The price of {self.name} is now {self.price} UAH.")

    def update_count(self, new_count: int) -> None:
        """Update the stock quantity of the product.

        :param new_count: The new stock quantity to be set.
        """
        if new_count < 0:
            raise ValueError("New stock quantity cannot be negative.")

        self.product_count = new_count

        print(f"The stock quantity of {self.name} is now {self.price}.")

    def __str__(self) -> str:
        """Return a string representation of the product."""
        return (f"\nThe product's name: {self.name} "
                f"\nThe product's category: {self.category}"
                f"\nThe product's price: {self.price}"
                f"\nThe product's count: {self.product_count}")


class Customer:
    """Represents a customer in the system."""

    def __init__(self, name: str, email: str, orders_list: list = None):
        """Initialize a new Customer instance.

        :param name: The name of the customer.
        :param email: The email address of the customer.
        :param orders_list: An optional initial list of orders. Defaults to an empty list.
        """
        self.name = name
        self.email = email
        self.orders_list = orders_list if orders_list is not None else []

    def add_order(self, order) -> None:
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