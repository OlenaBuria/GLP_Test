import pytest
import moment
import time
import allure

from Utils import utils as utils
from Scripts.loginInstructor import LoginInstructor
from Pages.Instructor.homePage import HomePage
from Pages.Instructor.homePageCopyCourse import HomePageCopyCourse
from Pages.Instructor.exchangePage import ExchangePage
from Scripts.copyCourseNameCSV import GetCopyCourseName
from Scripts.copyCourseName import CopyCourseName


@pytest.mark.usefixtures("test_setup")
class TestCopyCourse:

    def test_copy_existing_course_instructor(self):
        try:
            driver = self.driver
            login_instructor = LoginInstructor(driver)
            login_instructor.login_as_instructor()
            time.sleep(2)
            home_page = HomePage(driver)
            home_page.click_course_options()
            home_page.click_copy_course()
            exchange_page = ExchangePage(driver)
            time.sleep(2)
            exchange_page.click_next()
            exchange_page.check_online_course()
            exchange_page.click_course_start_date()
            exchange_page.select_current_date_box()
            exchange_page.click_course_end_date()
            exchange_page.click_next_calendar()
            exchange_page.click_next_calendar()
            exchange_page.click_next_calendar()
            exchange_page.click_next_calendar()
            exchange_page.select_28day_calendar()
            time.sleep(3)
            copy_course_name = CopyCourseName(driver)
            copy_course_name.get_copy_course_name()
            home_page = HomePage(driver)
            exchange_page.click_save()
            time.sleep(12)
            assert home_page.coach_mark_title() == "Done setting up your course dates and times?"
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
        time.sleep(2)
        home_page.click_link_got_it()
        time.sleep(2)
        try:
            driver = self.driver
            get_copy_course_name_csv = GetCopyCourseName(driver)
            home_page_copy_course = HomePageCopyCourse(driver)
            copy_course_name = "Copy of " + home_page_copy_course.get_text_copy_course()
            assert copy_course_name == get_copy_course_name_csv.get_copy_course_name()
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
        time.sleep(2)
