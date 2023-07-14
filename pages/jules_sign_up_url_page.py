from selenium.webdriver.common.by import By
from pages.base_page import PageUrl

class SignUpUp(PageUrl):
    Sign_up_button = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    Login_button = (By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[4]/a/button/span[1]')

    def navigate_to_login(self):
        self.driver.get("https://jules.app/sign-in")

    def sign_up_button(self):
        self.driver.find_element(*self.Sign_up_button).click()

    def log_in_button(self):
        self.driver.find_element(*self.Login_button).click()
