Feature: Login

    Scenario Outline: Components
        Given I load the website
        When I switch to device "<devices>"
        Then I see this component "Submit"
        Examples:
            | devices |
            |  1      |
            |  2      |


