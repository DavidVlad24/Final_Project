from selenium.webdriver.common.by import By
from browser import Browser


class FormAuth(Browser):
    FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')

    def navigate_to_form_auth(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def click_on_form_auth(self):
        self.driver.find_element(*self.FORM_AUTH).click()

    def check_url_form_auth(self):
        actual_url = "https://the-internet.herokuapp.com/login"
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url, "Url is incorrect"