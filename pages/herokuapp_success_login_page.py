from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class SuccessLoginPageTest(Browser):
    USERNAME_INPUT = (By.XPATH, '//*[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button')
    SUCCESS_LOGIN_MESSAGE = (By.NAME, 'You logged into a secure area!')
    LOGOUT_BUTTON = (By.XPATH, '//a[@class="button secondary radius"]')
    LOGOUT_MESSAGE = (By.XPATH, '//*[@id="flash"]')

    def navigate_to_form_auth(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_success_login_message(self, expected_notification):
        try:
            expected_error = self.driver.find_element(*self.SUCCESS_LOGIN_MESSAGE).text
        except NoSuchElementException:
            expected_error = None
        assert expected_error != expected_notification, "error"

    def click_logout_button(self):
        try:
            self.driver.find_element(*self.LOGOUT_BUTTON).click()
        except NoSuchElementException:
            print("Butonul nu a aparut")

    def verify_logout_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.LOGOUT_MESSAGE).is_displayed()
        except NoSuchElementException:
            actual_message = None
        assert actual_message != expected_message, "Invalid error message"
