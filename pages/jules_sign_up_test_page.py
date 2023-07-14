
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser
import threading

def wait(seconds):
    event = threading.Event()
    event.wait(seconds)


class SignUp(Browser):
    sign_up_button = (By.LINK_TEXT, 'Sign up.')
    personal_radio = (By.XPATH, '//input[@type="radio" and @value="personal"]')
    continue_button = (By.XPATH, '//button[@type="button" and @data-test-id="select-account-continue-btn"]')
    button_2 = (By.XPATH, '//button[@type="button" and @data-test-id="first-name-continue-btn"]')
    button_3 = (By.XPATH, '//button[@type="button" and @data-test-id="last-name-continue-btn"]')
    name_input = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    invalid_mail = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')



    def get_login_page(self):
        self.driver.get("https://jules.app/sign-in")

    def click_sign_in(self):
        self.driver.find_element(*self.sign_up_button).click()

    def click_personal_button(self):
        self.driver.find_element(*self.personal_radio).click()



    def click_continue_step_1(self):
        wait(2)
        self.driver.find_element(*self.continue_button).click()

    def input_username(self, username):
        wait(2)
        self.driver.find_element(*self.name_input).send_keys(username)



    def click_continue_step_2(self):
        wait(2)
        self.driver.find_element(*self.button_2).click()



    def input_lastname(self, lastname):
        wait(2)
        self.driver.find_element(*self.name_input).send_keys(lastname)



    def click_continue_step_3(self):
        wait(2)
        self.driver.find_element(*self.button_3).click()



    def wrong_email_input(self, mail):
        wait(2)
        self.driver.find_element(*self.name_input).send_keys(mail)



    def verify_wrong_mail_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.invalid_mail).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message != expected_message, "Enter valid mail"

    def clear_mail_input(self):
        self.driver.find_element(*self.name_input).clear()

    def correct_mail_input(self, c_mail):
        self.driver.find_element(*self.name_input).send_keys(c_mail)

    def not_displayed_invalid_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.invalid_mail).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message != expected_message, "Enter valid mail2"
