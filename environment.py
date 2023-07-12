from browser import Browser
from pages.forgot_pass_errors_page import ForgotPassError
from pages.forgot_pass_valid_page import ForgotPassValid
from pages.login_page import LoginPage
from pages.sign_up_url_page import SignUpUp
from pages.base_page import PageUrl
from pages.sign_up_test_page import SignUp
from pages.checkbox_url_page import Checkbox
from pages.login_test_page import LoginPageTest
from pages.form_auth_url_page import FormAuth
from pages.add_remove_elements_page import AddRemove


def before_all(context):
    context.browser = Browser()
    context.forgot_pass_errors_page = ForgotPassError()
    context.forgot_pass_valid_page = ForgotPassValid()
    context.login_page = LoginPage()
    context.sign_up_url_page = SignUpUp()
    context.base_page = PageUrl()
    context.sign_up_test_page = SignUp()
    context.checkbox_url_page = Checkbox()
    context.login_test_page = LoginPageTest()
    context.form_auth_url_page = FormAuth()
    context.add_remove_elements_page = AddRemove()

def after_all(context):
    context.browser.close()
