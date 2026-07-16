# Created by bbkam at 7/10/2026
Feature: Test for TV Mall search functionality

  Scenario: User can search for a product
    Given Open TVmall main page
    When Close pop up message
    When Search for a tea
    Then Verify correct search result shown for tea


  Scenario: User can search for a product
    Given Open TVmall main page
    When Close pop up message
    When Search for a jeans
    Then Verify correct search result shown for jeans


  Scenario Outline: User can search for a product
    Given Open TVmall main page
    When Close pop up message
    When Search for a <product>
    Then Verify correct search result shown for <product>

    Examples:
    |product |
    |shirt   |
    |pants   |
    |socks   |




