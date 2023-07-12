from behave import *

@Given("auth_url: I am on home page")
def step_impl(context):
    context.form_auth_url_page.navigate_to_form_auth()

@When("auth_url: I click on Form Authentication")
def step_impl(context):
    context.form_auth_url_page.click_on_form_auth()

@Then("auth_url: I verify if i am on Form Authentication page")
def step_impl(context):
    context.form_auth_url_page.check_url_form_auth()