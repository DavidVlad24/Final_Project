

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser

class ForgotPassValid(Browser):
    forgot_pass_button = (By.LINK_TEXT, 'Forgot password?')
    input = (By.XPATH, '//input[@placeholder="Enter your email"]')
    send_mail_button = (By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss34"]')
    mail_sent_notification = (By.XPATH, '//div[@id="client-snackbar"]')


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