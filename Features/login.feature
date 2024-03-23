Feature: Login Action
    Description: This feature will test a LogIn and LogOut functionality

Scenario Outline: Login with valid and invalid credentials
    Given User is on Home Page
    When User navigate to Login Page
    Then User enters "<username>" and "<password>"
    And Keeping case as "<case>"
    Then User should get logged in if "<case>" is Valid
    And Message displayed Login Successfully if "<case>" is Valid
    Then User will be asked to go back to login page if "<case>" is Invalid
    And Provide correct credentials if "<case>" is Invalid

Examples:
    | username       | password | case   |
    | abc@gmail.com  | 12345    | Valid  |
    | abc1@gmail.com | dfsd2    | Invalid|
