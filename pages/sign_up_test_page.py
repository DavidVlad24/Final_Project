from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser

class SignUp(Browser):
    sign_up_button = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    personal_radio = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[1]/span/input')
    continue_button = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button')
    button_2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button')
    button_3 = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button')
    name_input = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    invalid_mail = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')

    def get_login_page(self):
        self.driver.get("https://jules.app/sign-in")

    def click_sign_in(self):
        self.driver.find_element(*self.sign_up_button).click()

    def click_personal_button(self):
        self.driver.find_element(*self.personal_radio).click()

        sleep(2)

    def click_continue_step_1(self):
        self.driver.find_element(*self.continue_button).click()

    def input_username(self, username):
        self.driver.find_element(*self.name_input).send_keys(username)

        sleep(2)

    def click_continue_step_2(self):
        self.driver.find_element(*self.button_2).click()

        sleep(2)

    def input_lastname(self, lastname):
        self.driver.find_element(*self.name_input).send_keys(lastname)

        sleep(2)

    def click_continue_step_3(self):
        self.driver.find_element(*self.button_2).click()

        sleep(2)

    def wrong_email_input(self, mail):
        self.driver.find_element(*self.name_input).send_keys(mail)

        sleep(2)

    def verify_wrong_mail_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.invalid_mail).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, "Enter valid mail"

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
