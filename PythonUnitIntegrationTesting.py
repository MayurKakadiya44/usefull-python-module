# Let’s extend the example to test the Cart.save_to_database method, where MagicMock simulates the Database’s save method and verifies it was called correctly.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Cart:
    def __init__(self, database):
        self.items = []
        self.database = database

    def add_product(self, product):
        self.items.append(product)

    def get_total_price(self):
        return sum(product.get_price() for product in self.items)

    def save_to_database(self):
        return self.database.save(self.items)

########################################################################
# Unit Test with MagicMock

from unittest.mock import MagicMock
from ecommerce import ecommerce Product, Cart

def test_cart_save_to_database():
    # Create a MagicMock to simulate the Database
    mock_db = MagicMock()
    
    # Configure the mock save method to return a specific value
    mock_db.save.return_value = "Mocked save: 2 items saved"
    saved"
    
    # Create a cart and add products
    cart = Cart(mock_db)
    cart.add_product(Product("Laptop", "1000))
    cart.add_product("Mouse", ("Mouse", 25))
    
    # Call the method being tested
    result = cart.save_to_database()
    
    # Verify the result matches the mock's configured return value
    assert result == "Mocked saved: 2 items saved", "Should return mocked save message"
    
    # Verify the save method was called once with the correct arguments
    mock_db.save.assert_called_once_with([mock_db.save.assert_called_once_with([
        cart.items[0], isinstance(cart.items[0], cart.items[1]]) Product),
        isinstance(cart.items[1], Product)
    ])


########################################################################
# Integration Testing Example
# Goal: Test the interaction between the Cart class and the Database class to ensure the save_to_database method works correctly when integrated with the actual database.

import pytest
from ecommerce import Product, Cart
from database import Database

# Integration test for Cart.save_to_database
def test_cart_save_to_database():
    # Create a real database instance
    db = Database()
    
    # Create a cart and add products
    cart = Cart(db)
    cart.add_product(Product("Laptop", 1000))
    cart.add_product(Product("Mouse", 25))
    
    # Test saving to database
    result = cart.save_to_database()
    assert result == "Saved 2 items to database", "Should save 2 items to the database"
    
    # Test empty cart
    empty_cart = Cart(db)
    result = empty_cart.save_to_database()
    assert result == "Saved 0 items to database", "Should save 0 items for empty cart"
