# Created by bbkam at 7/10/2026
Feature: Test for TV Mall search functionality


  Scenario: User can access shopping cart
    Given Open TVmall main page
    When Click on shopping cart
    Then Verify cart is empty


  Scenario: User can search for a product
    Given Open TVmall main page
    When Search for a product
    Then Verify correct search result shown


  Scenario: User can access login page
    Given Open TVmall main page
    When Click on login icon
    Then Verify login page is open

