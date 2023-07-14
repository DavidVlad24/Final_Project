import time

from behave import *

@Given('Sign_Up: I open login page')
def step_impl(context):
    context.sign_up_test_page.get_login_page()

@When('Sign_Up: I click sign in')
def step_impl(context):
    context.sign_up_test_page.click_sign_in()

@When('Sign_Up: I click on personal check')
def step_impl(context):
    context.sign_up_test_page.click_personal_button()

@When('Sign_Up: I click continue_button_step_1')
def step_impl(context):
    context.sign_up_test_page.click_continue_step_1()

@When('Sign_Up: I put correct first name "{u_username}"')
def step_impl(context, u_username):
    context.sign_up_test_page.input_username(u_username)

@When('Sign_Up: I click continue_button_step_2')
def step_impl(context):
    context.sign_up_test_page.click_continue_step_2()

@When('Sign_Up: I put correct last name "{u_lastname}"')
def step_impl(context, u_lastname):
    context.sign_up_test_page.input_lastname(u_lastname)


@When('Sign_Up: I click continue_button_step_3')
def step_impl(context):
    context.sign_up_test_page.click_continue_step_3()


@When('Sign_Up: I put wrong email "{u_email}"')
def step_impl(context, u_email):
    context.sign_up_test_page.wrong_email_input(u_email)

@Then('Sign_Up: I verify if the msg is displayed "{msg1}"')
def step_impl(context, msg1):
    context.sign_up_test_page.verify_wrong_mail_message(msg1)

@Then('Sign_Up: I clear mail input')
def step_impl(context):
    context.sign_up_test_page.clear_mail_input()

@Then('Sign_Up: I put correct email address "{c_mail}"')
def step_impl(context, c_mail):
    context.sign_up_test_page.correct_mail_input(c_mail)

@Then('Sign_Up: I verify if the error msg is not displayed anymore ("{msg2}")')
def step_impl(context, msg2):
    context.sign_up_test_page.not_displayed_invalid_message(msg2)
