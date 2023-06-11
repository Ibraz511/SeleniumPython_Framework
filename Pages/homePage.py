from selenium.webdriver.common.by import By
from SeleniumPython_Framework.Locators.Locators import Locator
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu=Locator.menu
        self.logout_selector=Locator.logout_selector

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, self.menu).click()
        self.driver.find_element(By.LINK_TEXT, self.logout_selector).click()
