Feature: Login page functionality

  Scenario:
    Given Im on the login page
    When I put my correct mail "mail"
    When I i leave password field empty "password"
    Then I verify the error "Please enter your password!"
    Then I verify if login button is disabled


