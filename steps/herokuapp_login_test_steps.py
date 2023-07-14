from behave import *

@Given('login_auth: I am a user on login page 1')
def step_impl(context):
    context.herokuapp_login_test_page.navigate_to_form_auth()

@When('login_auth: I fill in my username with "{u_username}"')
def step_impl(context, u_username):
    context.herokuapp_login_test_page.set_username(u_username)

@When('login_auth: I fill in my password with "{p_password}"')
def step_impl(context, p_password):
    context.herokuapp_login_test_page.set_password(p_password)

@When('login_auth: Click login button 1')
def step_impl(context):
    context.herokuapp_login_test_page.click_login_button()

@Then('login_auth: I verify the invalid login username message "{msg1}"')
def step_impl(context, msg1):
    context.herokuapp_login_test_page.verify_invalid_username_message(msg1)

@Then('login_auth: I verify the invalid login password message "{msg2}"')
def step_impl(context, msg2):
    context.herokuapp_login_test_page.verify_invalid_password_message(msg2)

@Then('login_auth: Verify login message "{msg3}"')
def step_impl(context, msg3):
    context.herokuapp_login_test_page.verify_success_login_message(msg3)


