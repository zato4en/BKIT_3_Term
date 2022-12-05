Feature: Func create array with random counts
  Scenario: New array will contain random numbers from users interval
    Given Having numbers 20, 2, 4
    When Array got created with func gen_random
    Then Result should be an array with random numbers which set will be [2,3,4] (not 100% chance)