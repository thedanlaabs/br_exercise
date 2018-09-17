from br_locators import BRHomeLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def open_page(self):
        url = 'https://bleacherreport.com/'
        self.driver.get(url)

    def is_title_good(self):
        return "Bleacher" in self.driver.title

    def is_nfl_link_working(self):
        element = self.driver.find_element(*BRHomeLocators.nfl_button)
        element.click()
        return "NFL" in self.driver.title

