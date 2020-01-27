from selenium import webdriver
import pytest
import time
import allure
import moment
# import sys
# import os
# sys.path.append("/Users/vburiol/PycharmProjects/GLP_Test/Pages/")
# TEST_DIR = os.path.abspath(os.path.dirname(__file__))
# DIR = TEST_DIR.split('/GLP_Test')[0]
# os.chdir(DIR)
# paths = [DIR]
# sys.path = paths + sys.path


from Pages.Instructor.loginPage import LoginPage
from Pages.Instructor.homePage import HomePage
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_username(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            login.click_login()
            time.sleep(4)
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

        home_page = HomePage(driver)
        home_page.click_menu_instructor()
        home_page.click_account_settings()

        try:
            user_name_displayed = driver.find_element_by_id("displayedUsername").text
            assert user_name_displayed == utils.USERNAME

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except:
            print("There was an exception")
            raise

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_menu_instructor()
            homepage.click_logout()
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

# run tests
# python -m pytest
#
# python -m pytest --html=reports/report.html
#
# python -m pytest --alluredir=reports/allure-reports

# allure serve reports/allure-reports





