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
from Scripts.inviteURL import InviteURL
from Scripts.courseURL import CourseURL
from Pages.Instructor.diagnosticManagementPage import DiagnosticManagement
from Pages.Instructor.dashboardCoursePage import DashboardPage
from Pages.Instructor.createAssignmentPage import CreateAssignmentPage


@pytest.mark.usefixtures("test_setup")
class TestCreateCourse:

    def test_create_course_i(self):
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
        home_page.click_link_got_it()
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

    def student_locked_course_rio(self):  # RIO course - doesn't exist from 02/10/2020
        # Verify if locked course
        try:
            driver = self.driver
            time.sleep(1)
            home_page = HomePage(driver)
            home_page.click_name_created_course()
            diagnostic_management = DiagnosticManagement(driver)
            time.sleep(2)
            assert diagnostic_management.text_diagnostic_locked() == "The diagnostic is locked"
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
        diagnostic_management.pearson_logo_back_btn_click()

    def empty_performance_page_locked_course_rio(self):  #RIO course - doesn't exist from 02/10/2020
        #  Verify empty state if no students attempted the course and course locked
        driver = self.driver
        course_id_current = CourseURL(driver)
        course_id_current.get_course_url()
        time.sleep(2)
        driver.find_element_by_xpath("//*[contains(text(), 'PERFORMANCE')]").click()
        time.sleep(2)
        number_of_students = driver.find_element_by_css_selector(".c-chart-one .arc-value-max").text
        assert number_of_students == "0"
        time.sleep(1)
        class_proficiency_per_chapter = driver.find_element_by_css_selector(".overlay:nth-child(4) .large-lbl-b").text
        assert class_proficiency_per_chapter == "Start with an overview by chapter"
        students_most_challenging_objectives = driver.find_element_by_css_selector(".overlay:nth-child(3) > "
                                                                                   "div:nth-child(1) > "
                                                                                   ".large-lbl-b").text
        assert students_most_challenging_objectives == "See where to focus your efforts"
        list_of_students_with_proficient = driver.find_element_by_css_selector("div:nth-child(2) > .large-lbl-b").text
        assert list_of_students_with_proficient == "Drill down for student details"
        diagnostic_management = DiagnosticManagement(driver)
        diagnostic_management.pearson_logo_back_btn_click()

    def test_empty_dashboard_page_no_assignments_revel(self):
        try:
            driver = self.driver
            home_page = HomePage(driver)
            home_page.click_name_created_course()
            time.sleep(2)
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

    def test_create_publish_assignment(self):
        driver = self.driver
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
        dashboard_page.click_close_icon_on_success_popup()
        time.sleep(1)

    def test_student_enrollment_by_link(self):
        driver = self.driver
        invite_url = InviteURL(driver)
        invite_link = invite_url.get_invite_student_url()
        driver.execute_script("window.open('" + invite_link + "');")
        time.sleep(1)

    # def unlock_course(self):
    # # Verify user is able to unlock the course. Unable to lock it again
    #
    # def empty_performance_page_unlocked_course(self):
    # # Verify empty state if no students attempted the course and course unlocked
    #
    # def student_unlocked_course(self):
    # # Verify the student is able to start assessment if unlocked course
    #
    # def pla_in_performance_page_unlocked_course_students(self):
    # # Verify data is shown under performance page if student has finished the assessment











