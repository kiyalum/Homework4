# Task 1


class Product:
    """Represents a product in a store inventory."""

    def __init__(self, name, category, price, product_count):
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

    def __str__(self):
        """Return a string representation of the product."""
        return (f"\nThe product's name: {self.name} "
                f"\nThe product's category: {self.category}"
                f"\nThe product's price: {self.price}"
                f"\nThe product's count: {self.product_count}")