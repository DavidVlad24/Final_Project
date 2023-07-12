from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class ForgotPassError(Browser):
    forgot_pass_button = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/a')
    input = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/input')
    invalid_mail = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/p')
    send_mail_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/button')
    mail_sent_notification = (By.XPATH, '//*[@id="client-snackbar"]/div/div/span')

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
        assert actual_message == expected_message, "Enter valid mail"
