Feature: Integer Comparison

Scenario: Comparing two integers
  Given I have two integers, "a" and "b"
  When I compare the integers
  Then the outcome should be:
    | Comparison | Result |
    | a > b      | False  |
    | a < b      | True   |
    | a = b      | False  |

Scenario: Comparing two identical integers
  Given I have two identical integers, "a" and "a"
  When I compare the integers
  Then the outcome should be:
    | Comparison | Result |
    | a > a      | False  |
    | a < a      | False  |
    | a = a      | True   |