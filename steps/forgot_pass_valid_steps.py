from behave import *

@Given('forgot_pass_valid: I open login page')
def step_impl(context):
    context.forgot_pass_valid_page.navigate_to_main_page()

@When('forgot_pass_valid: Click on forgot password')
def step_impl(context):
    context.forgot_pass_valid_page.click_forgot_pass()

@When('forgot_pass_valid: Enter valid mail "{e_mail}"')
def step_impl(context, e_mail):
    context.forgot_pass_valid_page.enter_valid_mail(e_mail)

@Then('forgot_pass_valid: Click send mail')
def step_impl(context):
    context.forgot_pass_valid_page.click_send_mail()

@Then('forgot_pass_valid: Check mail sent notification "{msg2}"')
def step_impl(context, msg2):
    context.forgot_pass_valid_page.check_sent_mail_notification(msg2)