import os
from asyncio import wait
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser

class LoginPageTest(Browser):
    USERNAME_INPUT = (By.XPATH, '//*[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button')
    INVALID_USERNAME_MESSAGE = (By.NAME, "Your username is invalid!")
    INVALID_PASSWORD_MESSAGE = (By.NAME, 'Your password is invalid!')
    SUCCESS_LOGIN_MESSAGE = (By.NAME, 'You logged into a secure area!')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/a/i')
    LOGOUT_MESSAGE = (By.XPATH, '//*[@id="flash"]')

    def navigate_to_form_auth(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_invalid_username_message(self, expected_notification):
        try:
            expected_error = self.driver.find_element(*self.INVALID_USERNAME_MESSAGE).text
        except NoSuchElementException:
            expected_error = "None"
        assert expected_error != expected_notification, "Invalid username message is incorrect"

    def verify_invalid_password_message(self, expected_notification):
        try:
            expected_error = self.driver.find_element(*self.INVALID_PASSWORD_MESSAGE).text
        except NoSuchElementException:
            expected_error = None
        assert expected_error != expected_notification, "Invalid password message is incorrect"



