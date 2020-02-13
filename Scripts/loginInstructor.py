from Pages.Instructor.loginPage import LoginPage
from Utils import env


class LoginInstructor:

    def __init__(self, driver):
        self.driver = driver

    def login_as_instructor(self):
        driver = self.driver
        self.driver.get(env.URL)
        login = LoginPage(driver)
        login.enter_username(env.USERNAME)
        login.enter_password(env.PASSWORD)
        login.click_login()

