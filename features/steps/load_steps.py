######################################################################
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
######################################################################

"""
Product Steps

Steps file for products.feature

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import requests
from requests.models import Response
from requests import status_codes

# Load the database with new products
def load_products(context):
    rest_endpoint = 'http://your-api-endpoint/products'  # Replace with your actual API URL

    # Loop through each row in the BDD background table
    for row in context.table:
        # Prepare the payload (product details)
        payload = {
            "name": row['name'],
            "description": row['description'],
            "price": row['price'],
            "available": row['available'].lower() in ['true', '1'],  # Convert to boolean
            "category": row['category']
        }

        # Send POST request to add the product
        context.resp = requests.post(rest_endpoint, json=payload)

        # Assert that the response status is HTTP 201 Created
        assert context.resp.status_code == 201, f"Failed to create product {row['name']}"
