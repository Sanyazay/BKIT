Feature: Test summary
    Scenario: test summary for making check with 1 2 3
        Given ordering food with answers in bot first course - 1 main course - 2 dessert - 3
        When we form summary of check
        Then check should be with correct price 324
    Scenario: test summary for making check with 1 3 3
        Given ordering food with answers in bot first course - 1 main course - 3 dessert - 3
        When we form summary of check
        Then check should be with correct price 349
    Scenario: test summary for making check with 2 2 2
        Given ordering food with answers in bot first course - 2 main course - 2 dessert - 2
        When we form summary of check
        Then check should be with correct price 430

