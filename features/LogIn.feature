Feature: Login

    Scenario Outline: Components
        Given I load the website
        When I switch to device "1"
        Then I see component "<Component>" with attribute "<Attribute>"
        Examples:
            | Component    | Attribute |
            |  Submit      | disabled  |
            |  Player Name | enabled   |


