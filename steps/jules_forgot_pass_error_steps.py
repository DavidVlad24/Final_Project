from behave import *

@Given('forgot_pass_error: I open login page')
def step_impl(context):
    context.forgot_pass_errors_page.navigate_to_main_page()

@When('forgot_pass_error: Click on forgot password')
def step_impl(context):
    context.forgot_pass_errors_page.click_forgot_pass()

@When('forgot_pass_error: Enter invalid mail "{mail}"')
def step_impl(context, mail):
    context.forgot_pass_errors_page.enter_invalid_mail(mail)

@Then('forgot_pass_error: Check invalid mail error "{msg1}"')
def step_impl(context, msg1):
    context.forgot_pass_errors_page.check_wrong_mail_notification(msg1)