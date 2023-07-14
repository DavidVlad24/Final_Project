from behave import *

@Given('success_login_auth: I am a user on login page 1')
def step_impl(context):
    context.herokuapp_success_login_page.navigate_to_form_auth()

@When('success_login_auth: I fill in my username with "{u_username}"')
def step_impl(context, u_username):
    context.herokuapp_success_login_page.set_username(u_username)

@When('success_login_auth: I fill in my password with "{p_password}"')
def step_impl(context, p_password):
    context.herokuapp_success_login_page.set_password(p_password)

@When('success_login_auth: Click login button 1')
def step_impl(context):
    context.herokuapp_success_login_page.click_login_button()

@Then('success_login_auth: Verify login message "{msg3}"')
def step_impl(context, msg3):
    context.herokuapp_success_login_page.verify_success_login_message(msg3)

@Then('success_login_auth: I click on log out buttton')
def step_impl(context):
    context.herokuapp_success_login_page.click_logout_button()

@Then('success_login_auth: We check the log out message "{msg4}"')
def step_impl(context, msg4):
    context.herokuapp_success_login_page.verify_logout_message(msg4)