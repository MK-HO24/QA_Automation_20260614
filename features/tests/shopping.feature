# Created by bbkam at 7/16/2026
Feature: Test for shopping experience
  # Enter feature description here

  Scenario: Verify that use is able to add product to cart
    Given Open TVmall main page
    When Search for a shirt
    When Add item to cart
    Then Verify that item is added to cart