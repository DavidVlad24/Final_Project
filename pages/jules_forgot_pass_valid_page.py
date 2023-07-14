

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser

class ForgotPassValid(Browser):
    forgot_pass_button = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/a')
    input = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/input')
    send_mail_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/button')
    mail_sent_notification = (By.XPATH, '//*[@id="client-snackbar"]/div/div/span')
    invalid_mail = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/p')

    def navigate_to_main_page(self):
        self.driver.get("https://jules.app/sign-in")

    def click_forgot_pass(self):
        self.driver.find_element(*self.forgot_pass_button).click()

    def enter_valid_mail(self, c_mail):
        self.driver.find_element(*self.input).send_keys(c_mail)

    def click_send_mail(self):
        self.driver.find_element(*self.send_mail_button).click()


    def check_sent_mail_notification(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.mail_sent_notification).is_displayed()
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message != expected_message, "Message not displayed"