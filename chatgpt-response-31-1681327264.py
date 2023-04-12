Feature: Integer addition
  As a user
  I want to add two integers together
  So that I can know the correct outcome

  Background:
    Given a calculator app is running

  Scenario: Add two integers
    Given I have entered a first integer into the calculator
    And I have entered a second integer into the calculator
    When I press the add button
    Then the correct addition outcome should be displayed on the screen

    Examples:
      | first_integer | second_integer | outcome |
      | 10            | 20             | 30      |
      | -15           | 25             | 10      |
      | 0             | 0              | 0       |