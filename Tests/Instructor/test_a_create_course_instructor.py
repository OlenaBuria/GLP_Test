import pytest
import csv

from Utils import env
import moment
import time
import allure
from Utils import utils as utils
from Scripts.loginInstructor import LoginInstructor
from Pages.Instructor.homePage import HomePage
from Pages.Instructor.materialsSearchPage import SearchMaterialsPage
from Pages.Instructor.exchangePage import ExchangePage
from Pages.Instructor.dashboardCoursePage import DashboardPage
from Pages.Student.homePageStudent import HomePageStudent


@pytest.mark.usefixtures("test_setup")
class TestCreateCourse:

    def test_create_course_instructor(self):
        # Login
        try:
            driver = self.driver
            login_instructor = LoginInstructor(driver)
            login_instructor.login_as_instructor()
            # Create course
            search_materials = SearchMaterialsPage(driver)
            search_materials.click_search_materials()
            search_materials.input_pearson_materials(env.CourseMaterial)
            search_materials.click_search_icon()
            search_materials.select_pearson_material()
            time.sleep(3)
            assert search_materials.name_found_material() == env.CourseMaterial
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
        search_materials.click_create_course()
        exchange_page = ExchangePage(driver)
        exchange_page.click_section_title()
        exchange_page.input_section_title(utils.SectionTitle)
        time.sleep(2)
        exchange_page.click_next()
        exchange_page.click_section_code()
        exchange_page.input_section_code(utils.SectionTitle)
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
        try:
            assert home_page.coach_mark_title() == "Done setting up your course dates and times?"
            home_page.click_link_got_it()
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

        with open('/Users/vburiol/Documents/AutomationOutput/CourseName.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Course Name'])
            writer.writerow([utils.SectionTitle])
        time.sleep(2)
        try:
            assert home_page.name_created_course_text() == utils.SectionTitle
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

    def test_launch_created_course_instructor(self):
        try:
            driver = self.driver
            home_page_student = HomePageStudent(driver)
            home_page_student.click_course_name()
            time.sleep(2)
            dashboard_page = DashboardPage(driver)
            assert home_page_student.get_course_name_home_page() == dashboard_page.get_text_course_name()
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

    def test_empty_course_dashboard_page_no_assignments_instructor(self):
        try:
            driver = self.driver
            dashboard_page = DashboardPage(driver)
            assert dashboard_page.no_assignments_yet() == "Encourage reading, practice, and review"
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













