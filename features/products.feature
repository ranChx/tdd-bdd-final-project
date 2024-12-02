Feature: The product store service back-end
    As a Product Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name       | description     | price   | available | category   |
        | Hat        | A red fedora    | 59.95   | True      | CLOTHS     |
        | Shoes      | Blue shoes      | 120.50  | False     | CLOTHS     |
        | Big Mac    | 1/4 lb burger   | 5.99    | True      | FOOD       |
        | Sheets     | Full bed sheets | 87.00   | True      | HOUSEWARES |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Product Catalog Administration" in the title
    And I should not see "404 Not Found"
    
Scenario: Read a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red fedora" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "Cloths" in the "Category" dropdown
    And I should see "59.95" in the "Price" field

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I click the "Edit" button for "Hat"
    And I update the "Price" to "69.95"
    And I press the "Save" button
    Then I should see the message "Product updated successfully"
    And I should see "69.95" in the "Price" field

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I click the "Delete" button for "Hat"
    And I confirm the deletion
    Then I should see the message "Product deleted successfully"
    And I should not see "Hat" in the product list

Scenario: List all Products
    When I visit the "Home Page"
    And I press the "List All" button
    Then I should see a list of products
    And I should see "Hat" in the list
    And I should see "Shoes" in the list
    And I should see "Shirt" in the list

Scenario: Search for Products by Category
    When I visit the "Home Page"
    And I set the "Category" to "Cloths"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the product list
    And I should see "Shirt" in the product list
    And I should not see "Laptop" in the product list

Scenario: Search for Products by Availability
    When I visit the "Home Page"
    And I set the "Available" dropdown to "True"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the product list
    And I should see "Shirt" in the product list
    And I should not see "Laptop" in the product list

Scenario: Search for Products by Name
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the product list
    And I should not see "Shirt" in the product list
    And I should not see "Shoes" in the product list


