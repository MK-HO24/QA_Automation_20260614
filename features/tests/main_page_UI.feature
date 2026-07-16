# Created by bbkam at 7/15/2026
Feature: User can test main page UI
  # Enter feature description here

  Scenario: Verify header has correct amount of links
    Given Open TVmall main page
    When Verify header has 5 links


  Scenario: Verify header is shown
    Given Open TVmall main page
    When Verify header is shown
    And Verify header has links