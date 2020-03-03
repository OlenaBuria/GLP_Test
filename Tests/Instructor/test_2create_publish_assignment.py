import pytest

import moment
import time
import allure
from Utils import utils as utils
from Scripts.loginInstructor import LoginInstructor
from Pages.Instructor.dashboardCoursePage import DashboardPage
from Pages.Instructor.createAssignmentPage import CreateAssignmentPage
from Pages.Student.homePageStudent import HomePageStudent


@pytest.mark.usefixtures("test_setup")
class TestCreatePublishAssignment:

    def test_create_publish_assignment_instructor(self):
        try:
            driver = self.driver
            login_instructor = LoginInstructor(driver)
            login_instructor.login_as_instructor()
            home_page_student = HomePageStudent(driver) # verify
            home_page_student.click_course_name() # verify
            dashboard_page = DashboardPage(driver)
            dashboard_page.click_create_assignment()
            time.sleep(2)
            create_assignment = CreateAssignmentPage(driver)
            create_assignment.click_chapter1()
            time.sleep(2)
            create_assignment.click_select_all()
            time.sleep(2)
            create_assignment.click_add_content()
            time.sleep(2)
            create_assignment.click_due_date()
            create_assignment.click_next_month()
            create_assignment.select_day28_calendar()
            time.sleep(2)
            create_assignment.click_publish_assignment()
            time.sleep(3)
            success_popup = dashboard_page.success_popup_published_assignment()
            assert success_popup == "You successfully published your assignment."
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
        dashboard_page.click_close_icon_on_success_popup()
        time.sleep(1)
