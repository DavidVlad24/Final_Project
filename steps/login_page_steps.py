from behave import *

@Given('Im on the login page')
def step_impl(context):
    context.login_page.navigate_to_login()
@When('I put my correct mail "{mail}')
def step_impl(context, mail):
    context.login_page.input_correct_mail(mail)
@When('I i leave password field empty "{password}"')
def step_impl(context, password):
    context.login_page.input_password(password)
@Then('I verify the error "{msg1}"')
def step_impl(context, msg1):
    context.login_page.invalid_password_message(msg1)
@Then('I verify if login button is disabled')
def step_impl(context):
    context.login_page.login_button_disabled()