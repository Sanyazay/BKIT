Feature: TestingTruck
    Scenario: test truck for making delivery
        Given ordering delivery for box with parametres deliverytype: "Экспресс" boxtype: "безопасная(для хрупких грузов)" weight: "57"
        When we create truck delivery
        Then delivery check should be with given parameters