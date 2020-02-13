from Pages.Instructor.homePage import HomePage


class LogOutInstructor:

    def __init__(self, driver):
        self.driver = driver

    def logout_as_instructor(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_menu_instructor()
        homepage.click_logout()
