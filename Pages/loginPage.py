from selenium.webdriver.common.by import By

from SeleniumPython_Framework.Locators.Locators import Locator
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = Locator.username #note that we used the classname.attribute since the base class (Locators) does not have any method
        self.password = Locator.password
        self.login_button = Locator.login_button
        self.invalidUsernameLocator=Locator.invalidUsernameLocator

    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.TAG_NAME, self.login_button).click()

    def invalidUsername(self):
        msg=self.driver.find_element(By.XPATH, self.invalidUsernameLocator).text
        return msg