from behave import *

@Given('I am on login page')
def step_impl(context):
    context.sign_up_url_page.navigate_to_login()

@When('I press Sign up')
def step_impl(context):
    context.sign_up_url_page.sign_up_button()

@Then('I verify the url to be "{u_url}"')
def step_impl(context, u_url):
    context.base_page.check_the_current_url(u_url)

@Then('I click on Log in button')
def step_impl(context):
    context.sign_up_url_page.log_in_button()

@Then('I verify the url on login to be "{url}"')
def step_impl(context, url):
    context.base_page.check_signin_url(url)