import csv
from Pages.Instructor.loginPage import LoginPage
from Utils import env


class LoginStudent:

    def __init__(self, driver):
        self.driver = driver

    def login_as_student(self):
        driver = self.driver
        self.driver.get(env.URL)
        login = LoginPage(driver)
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/StudentData.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                student_user_name = row["Student User Name"]
                student_password = row["Password"]
                login.enter_username(student_user_name)
                login.enter_password(student_password)
        reader.close()
        login.click_login()

    def get_student_user_name(self):
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/StudentData.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                student_user_name = row["Student User Name"]
                return student_user_name
        reader.close()