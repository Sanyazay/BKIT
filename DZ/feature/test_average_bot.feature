Feature: Test average
    Scenario: test average for making check with 1 2 3
        Given ordering1 food with answers in bot first course - 1 main course - 2 dessert - 3
        When we form average price of position of check
        Then average price should 108
