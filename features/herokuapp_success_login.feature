Feature: Success login functionality

Scenario: I fill in username and password
  Given success_login_auth: I am a user on login page 1
  When success_login_auth: I fill in my username with "username"
  When success_login_auth: I fill in my password with "password"
  When success_login_auth: Click login button 1
  Then success_login_auth: Verify login message "You logged into a secure area!"
  Then success_login_auth: I click on log out buttton
  Then success_login_auth: We check the log out message "You logged out of the secure area!"