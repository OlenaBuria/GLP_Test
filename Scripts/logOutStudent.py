from Pages.Student.homePageStudent import HomePageStudent


class LogOutStudent:

    def __init__(self, driver):
        self.driver = driver

    def logout_as_student(self):
        driver = self.driver
        homepage = HomePageStudent(driver)
        homepage.click_menu_student()
        homepage.click_sign_out()
