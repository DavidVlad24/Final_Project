Feature: Login functionality


Scenario Outline: Check various pass and usernames
      Given login_auth: I am a user on login page 1
      When login_auth: I fill in my username with "<username>"
      When login_auth: I fill in my password with "<password>"
      When login_auth: Click login button 1
      Then login_auth: I verify the invalid login username message "<expected_error>!"
      Then login_auth: I verify the invalid login password message "<expected_error>"


  Examples:
        | username     | password           |  expected_error            |     expected_notification      |
        | Username1    | Password1          | Your username is invalid!  |            None                |
        | None         |  None              | Your username is invalid!  |            None                |
        | tomsmith     |Password2           | Your password is invalid!  |            None                |
        | Username1    |SuperSecretPassword!| Your username is invalid!  |            None                |
