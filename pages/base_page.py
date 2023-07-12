from browser import Browser


class PageUrl(Browser):

    def check_the_current_url(self, url):
        actual = self.driver.current_url
        assert actual == url, f"Url-ul este gresit"

    def check_signin_url(self, url):
        actual_url = "https://jules.app/sign-in"
        assert actual_url == url, "Url not working"
