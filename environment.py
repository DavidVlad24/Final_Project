from browser import Browser
from pages.jules_forgot_pass_errors_page import ForgotPassError
from pages.jules_forgot_pass_valid_page import ForgotPassValid
from pages.jules_login_page import LoginPage
from pages.jules_sign_up_url_page import SignUpUp
from pages.base_page import PageUrl
from pages.jules_sign_up_test_page import SignUp
from pages.herokuapp_checkbox_url_page import Checkbox
from pages.herokuapp_login_test_page import LoginPageTest
from pages.herokuapp_form_auth_url_page import FormAuth
from pages.herokuapp_add_remove_elements_page import AddRemove
from pages.herokuapp_success_login_page import SuccessLoginPageTest


def before_all(context):
    context.browser = Browser()
    context.jules_forgot_pass_errors_page = ForgotPassError()
    context.jules_forgot_pass_valid_page = ForgotPassValid()
    context.jules_login_page = LoginPage()
    context.jules_sign_up_url_page = SignUpUp()
    context.base_page = PageUrl()
    context.jules_sign_up_test_page = SignUp()
    context.herokuapp_checkbox_url_page = Checkbox()
    context.herokuapp_login_test_page = LoginPageTest()
    context.herokuapp_form_auth_url_page = FormAuth()
    context.herokuapp_add_remove_elements_page = AddRemove()
    context.herokuapp_success_login_page = SuccessLoginPageTest()

def after_all(context):
    context.browser.close()
