Feature: Func create array with counts for rule: i + i**2
  Scenario: New array will contain modified numbers from users interval
    Given Having interval 2-4
    When Array got created with func squared_cont
    Then Result should be an array with numbers (i + i**2) for each i in given interval