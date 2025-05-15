
# Test Automation Framework

This project contains automated tests for the SauceDemo UI and AirportGap API.

## Setup

1. Install Python 3.8 or higher (developed and tested with Python 3.12.9)
2. Install dependencies:
```
pip install -r requirements.txt
``` 

## Running Tests

To run UI tests:
```
pytest UI_tests
``` 

To run API tests:
```
pytest API_tests 
``` 

To run all tests:
```
pytest
```
This framework implements all the required test scenarios using Python with:
- Selenium WebDriver for UI testing
- Requests library for API testing
- Pytest as the test runner
- Page Object Model design pattern for UI tests

## Test scenarios:
Scenario 1: Verify Inventory Items
1. Navigate to https://www.saucedemo.com and log in using the following
credentials:
   1. Username: standard_user
   2. Password: secret_sauce
2. Verify that the inventory page displays exactly 6 items.

Scenario 2: Add Item to Cart
1. Log in as described in Scenario 1.
2. Add the first inventory item to the shopping cart.
3. Verify that the cart badge correctly displays the number 1.