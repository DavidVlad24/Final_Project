from behave import *

@Given("Home_page: I am on home page")
def step_impl(context):
    context.herokuapp_checkbox_url_page.navigate_to_checkbox()

@When("Home_page: I click on checkbox")
def step_impl(context):
    context.herokuapp_checkbox_url_page.click_on_checkbox()

@Then("Home_page: I verify if i am on checkbox page")
def step_impl(context):
    context.herokuapp_checkbox_url_page.check_url_checkbox()