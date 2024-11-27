# Copyright 2016, 2023 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test cases for Product Model

Test cases can be run with:
    nosetests
    coverage report -m

While debugging just these tests it's convenient to use this:
    nosetests --stop tests/test_models.py:TestProductModel

"""
import unittest
from service.models import Product, Category
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    
    def test_create_product(self):
        """It should create a product and verify that it has been created with correct properties."""
        product = ProductFactory.create()  # Use factory to create product
        self.assertIsNotNone(product.id)  # Check that ID is not None
        self.assertEqual(product.name, product.name)  # Check name matches
        self.assertEqual(product.description, product.description)  # Check description matches
        self.assertEqual(product.price, product.price)  # Check price matches
        self.assertEqual(product.available, product.available)  # Check availability
        self.assertEqual(product.category, product.category)  # Check category

    def test_read_product(self):
        """It should read a product from the database and verify its properties."""
        product = ProductFactory.create()
        product_id = product.id  # Save the ID for later comparison
        
        # Retrieve the product from the database
        found_product = Product.query.get(product_id)
        
        self.assertEqual(found_product.id, product_id)  # Ensure the ID matches
        self.assertEqual(found_product.name, product.name)  # Ensure name matches
        self.assertEqual(found_product.description, product.description)  # Ensure description matches
        self.assertEqual(found_product.price, product.price)  # Ensure price matches
        self.assertEqual(found_product.available, product.available)  # Ensure availability matches
        self.assertEqual(found_product.category, product.category)  # Ensure category matches

    def test_update_product(self):
        """It should update the product's description."""
        product = ProductFactory.create()
        original_id = product.id
        original_description = product.description
        
        # Update the description
        product.description = "Updated description"
        product.save()

        updated_product = Product.query.get(original_id)

        self.assertEqual(updated_product.id, original_id)  # Ensure ID is the same
        self.assertNotEqual(updated_product.description, original_description)  # Ensure description is updated
        self.assertEqual(updated_product.description, "Updated description")  # Ensure the new description matches

    def test_delete_product(self):
        """It should delete the product from the database."""
        product = ProductFactory.create()
        product_id = product.id
        
        # Ensure the product exists
        self.assertIsNotNone(Product.query.get(product_id))
        
        # Delete the product
        product.delete()
        
        # Ensure the product is deleted
        self.assertIsNone(Product.query.get(product_id))

    def test_list_all_products(self):
        """It should list all products in the database."""
        ProductFactory.create_batch(5)  # Create 5 products
        products = Product.query.all()
        
        # Ensure there are 5 products in the database
        self.assertEqual(len(products), 5)

    def test_find_by_name(self):
        """It should find products by their name."""
        products = ProductFactory.create_batch(5)  # Create 5 products
        name_to_search = products[0].name  # Get name of the first product
        
        # Find products by name
        found_products = Product.find_by_name(name_to_search)
        
        # Ensure the count matches the number of products with that name
        self.assertEqual(len(found_products), sum(1 for p in products if p.name == name_to_search))
        
        # Ensure all found products have the correct name
        for product in found_products:
            self.assertEqual(product.name, name_to_search)

    def test_find_by_availability(self):
        """It should find products by availability."""
        products = ProductFactory.create_batch(10)  # Create 10 products
        availability_to_search = products[0].available  # Get availability of the first product
        
        # Find products by availability
        found_products = Product.find_by_availability(availability_to_search)
        
        # Ensure the count matches the number of products with that availability
        self.assertEqual(len(found_products), sum(1 for p in products if p.available == availability_to_search))
        
        # Ensure all found products have the correct availability
        for product in found_products:
            self.assertEqual(product.available, availability_to_search)

    def test_find_by_category(self):
        """It should find products by category."""
        products = ProductFactory.create_batch(10)  # Create 10 products
        category_to_search = products[0].category  # Get category of the first product
        
        # Find products by category
        found_products = Product.find_by_category(category_to_search)
        
        # Ensure the count matches the number of products with that category
        self.assertEqual(len(found_products), sum(1 for p in products if p.category == category_to_search))
        
        # Ensure all found products have the correct category
        for product in found_products:
            self.assertEqual(product.category, category_to_search)

if __name__ == '__main__':
    unittest.main()
