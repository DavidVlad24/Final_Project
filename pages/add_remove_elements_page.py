from selenium.webdriver.common.by import By
from browser import Browser

class AddRemove(Browser):
    ADD_REMOVE_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')

    def navigate_to_add_remove_elements(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def click_on_add_remove_elements(self):
        self.driver.find_element(*self.ADD_REMOVE_ELEMENTS).click()

    def check_url_add_remove_elements(self):
        actual_url = "https://the-internet.herokuapp.com/add_remove_elements/"
        expected_url = "https://the-internet.herokuapp.com/add_remove_elements/"
        assert actual_url == expected_url, "Url is incorrect"