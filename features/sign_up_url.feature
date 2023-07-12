Feature: Sign Up url check

  Scenario:
    Given I am on login page
    When I press Sign up
    Then I verify the url to be "https://jules.app/sign-up"
    Then I click on Log in button
    Then I verify the url on login to be "https://jules.app/sign-in"