import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..","..")) #this is needed since we are importing classes from other files in this project and we wanna execute this script from CLI
from SeleniumPython_Framework.Pages.loginPage import LoginPage
from SeleniumPython_Framework.Pages.homePage import HomePage


class Login(unittest.TestCase): #inherit from the unittest class to make this project a unittest project

    @classmethod #we are stating that the setUpClass is a class method so that it can called using either the className or the methodName. This is needed to be done for the setUpClass and tearDownCLass methods
    def setUpClass(cls): # setUpClass is a built in class that has cls(Class) as its argument. This class acts similar to the before() in cypress
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Ibrahim F A/Documents/SELENIUM PYTHON/Base")
        cls.driver.maximize_window()  # This is used to maximize the window
        cls.driver.implicitly_wait(10)

    def test_valid_login(self): #first test case
        driver=self.driver #we did this so we dont have to always include self when trying to call driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home= HomePage(driver)
        home.logout()

    def test_wrongUsername_login(self): #second test case
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login=LoginPage(driver)
        login.enter_username("Ibrahim")
        login.enter_password("admin123")
        login.click_login()
        #I intentionally want to have a failed case
        self.assertEqual(login.invalidUsername() , "Invalid credentials") #true, to test for failure, edit the expected message to something wrong and the report will contain a failure

    @classmethod
    def tearDownClass(cls): #this method acts similar to after() in cypress
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/Ibrahim F A/Documents/SELENIUM PYTHON/SeleniumPython_Framework/Reports'))

