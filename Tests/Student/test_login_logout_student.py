import pytest
import time
import allure
import moment
from Scripts.loginStudent import LoginStudent
from Scripts.logOutStudent import LogOutStudent
from Pages.Student.homePageStudent import HomePageStudent
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login_student(self):
        try:
            driver = self.driver
            login_student = LoginStudent(driver)
            login_student.login_as_student()
            time.sleep(10)
            home_page = driver.title
            assert home_page == "Course Materials | Pearson"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("_%m-%d-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                                               + ".png")
            raise

        except:
            print("There was an exception")
            curr_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S_")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                                               + ".png")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute")

        home_page_student = HomePageStudent(driver)
        home_page_student.click_menu_student()
        home_page_student.click_account_settings_menu()

        try:
            user_name_displayed = home_page_student.displayed_user_name_menu()
            assert str.capitalize(user_name_displayed) == login_student.get_student_user_name()

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except:
            print("There was an exception")
            raise

    def test_logout_student(self):
        try:
            driver = self.driver
            logout_as_instructor = LogOutStudent(driver)
            logout_as_instructor.logout_as_student()
            time.sleep(4)
            login_page = driver.title
            assert login_page == "Pearson Sign In"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S_")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                                               + ".png")
            raise

        except:
            print("There was an exception")
            curr_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S_")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                                               + ".png")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute")