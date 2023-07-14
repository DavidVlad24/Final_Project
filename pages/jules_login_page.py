from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class LoginPage(Browser):
    email_input = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input')
    password_input = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
    invalid_error_message = (By.XPATH, '//*[@id="client-snackbar"]/div/span')
    invalid_password_none_message = (By.NAME, 'Please enter your password!')
    login_button = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button')

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
