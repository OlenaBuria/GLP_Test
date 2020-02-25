import pytest
import csv
import moment
import time
import allure

from Utils import utils as utils
from Scripts.loginInstructor import LoginInstructor
from Pages.Instructor.homePage import HomePage
from Pages.Instructor.exchangePage import ExchangePage


@pytest.mark.usefixtures("test_setup")
class TestCopyCourse:

    def test_copy_course(self):
        try:
            driver = self.driver
            login_instructor = LoginInstructor(driver)
            login_instructor.login_as_instructor()
            time.sleep(2)
            home_page = HomePage(driver)
            home_page.click_course_options()
            home_page.click_copy_course()
            exchange_page = ExchangePage(driver)
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
            time.sleep(2)
            exchange_page.click_save()
            home_page = HomePage(driver)
            time.sleep(4)
            with open('/Users/vburiol/Documents/AutomationOutput/CopyCourseName.csv', mode='w') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Copy Course Name'])
                writer.writerow(["Copy of " + utils.SectionTitle])
            home_page.click_link_got_it()
            assert home_page.name_created_course_text() == "Copy of " + utils.SectionTitle
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
