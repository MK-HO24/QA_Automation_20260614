# Created by bbkam at 7/11/2026
Feature: Tests for cart features


  Scenario: User can access shopping cart
    Given Open TVmall main page
    When Click on shopping cart
    Then Verify cart is empty