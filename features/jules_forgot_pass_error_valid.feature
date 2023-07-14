Feature: Forgot password errors testing

  Scenario:
    Given forgot_pass_error: I open login page
    When forgot_pass_error: Click on forgot password
    When forgot_pass_error: Enter invalid mail "mail"
    Then forgot_pass_error: Check invalid mail error "Please enter a valid email address!"

    Scenario:
      Given forgot_pass_valid: I open login page
      When forgot_pass_valid: Click on forgot password
      When forgot_pass_valid: Enter valid mail "mail@yahoo.com"
      Then forgot_pass_valid: Click send mail
      Then forgot_pass_valid: Check mail sent notification "Email Sent"