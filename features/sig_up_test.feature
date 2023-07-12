Feature: Sign up function

  Scenario:
    Given Sign_Up: I open login page
    When Sign_Up: I click sign in
    When Sign_Up: I click on personal check
    When Sign_Up: I click continue_button_step_1
    When Sign_Up: I put correct first name "Marinica"
    When Sign_Up: I click continue_button_step_2
    When Sign_Up: I put correct last name "Namol"
    When Sign_Up: I click continue_button_step_3
    When Sign_Up: I put wrong email "email"
    Then Sign_Up: I verify if the msg is displayed "Please enter a valid email address."
    Then Sign_Up: I clear mail input
    Then Sign_Up: I put correct email address "e_email@yahoo.com"
    Then Sign_Up: I verify if the error msg is not displayed anymore ("Please enter a valid email address.")