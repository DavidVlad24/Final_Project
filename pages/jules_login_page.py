from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class LoginPage(Browser):
    email_input = (By.XPATH, '//input[@placeholder="Enter your email"]')
    password_input = (By.XPATH, '//input[@placeholder="Enter your password"]')
    invalid_error_message = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')
    invalid_password_none_message = (By.NAME, 'Please enter your password!')
    login_button = (By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss16"]')

    def navigate_to_login(self):
        self.driver.get("https://jules.app/sign-in")

    def input_correct_mail(self, mail):
        self.driver.find_element(*self.email_input).send_keys(mail)
    def input_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def invalid_password_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.invalid_password_none_message).text
        except NoSuchElementException:
            actual_message = None
        assert actual_message != expected_message, "Invalid error message"

    def login_button_disabled(self):
        try:
            button = self.driver.find_element(*self.login_button)
            return not button.is_enabled()
        except NoSuchElementException:
            return True
