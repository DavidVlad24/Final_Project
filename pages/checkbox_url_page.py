from selenium.webdriver.common.by import By
from browser import Browser


class Checkbox(Browser):
    CHECKBOX = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')

    def navigate_to_checkbox(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def click_on_checkbox(self):
        self.driver.find_element(*self.CHECKBOX).click()

    def check_url_checkbox(self):
        actual_url = "https://the-internet.herokuapp.com/checkboxes"
        expected_url = "https://the-internet.herokuapp.com/checkboxes"
        assert actual_url == expected_url, "Url is incorrect"