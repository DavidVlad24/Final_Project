from behave import *

@Given("AddRemove: I am on home page")
def step_impl(context):
    context.add_remove_elements_page.navigate_to_add_remove_elements()

@When("AddRemove: I click on Add/Remove Elements")
def step_impl(context):
    context.add_remove_elements_page.click_on_add_remove_elements()

@Then("AddRemove: I verify if i am on Add/Remove Elements page")
def step_impl(context):
    context.add_remove_elements_page.check_url_add_remove_elements()