Feature: Login

    Scenario Outline: Components
        Given I load the website
        When I switch to device "1"
        Then I see component "<Component>" with attribute "<Attribute>"
        Examples:
            | Component    | Attribute  |
            |  Submit      | disabled   |
            |  Player Name | enabled    |

    Scenario: Submit is enabled after Player is entered
        Given I load the website
        When I switch to device "1"
        And I populate "Player Name" with "Matsuri"
        Then I see component "Submit" with attribute "enabled"

    Scenario: User can add player
        Given I load the website
        When I switch to device "1"
        And I populate "Player Name" with "Matsuri"
        And I click on "Submit"
        Then I see component "All Players Ready" with attribute "enabled"
        And I see "Player Info" with text "Matsuri" on screen
        