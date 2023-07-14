from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class ForgotPassError(Browser):
    forgot_pass_button = (By.LINK_TEXT, 'Forgot password?')
    input = (By.XPATH, '//input[@placeholder="Enter your email"]')
    invalid_mail = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')
    send_mail_button = (By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss34"]')
    mail_sent_notification = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')

    def navigate_to_main_page(self):
        self.driver.get("https://jules.app/sign-in")

    def click_forgot_pass(self):
        self.driver.find_element(*self.forgot_pass_button).click()

    def enter_invalid_mail(self, e_mail):
        self.driver.find_element(*self.input).send_keys(e_mail)

    def check_wrong_mail_notification(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.invalid_mail).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message != expected_message, "Enter valid mail"
