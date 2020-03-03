import pytest
import csv
import time
import random
import moment
import allure
from Pages.Instructor.loginPage import LoginPage
from Pages.Student.createAccountPage import CreateAccountPage
from Utils import utils as utils
from Utils import env
from selenium.webdriver.common.keys import Keys
from Utils import randomNames as randomNames
from Pages.Student.assignmentsPage import AssignmentsPage
from Pages.Student.homePageStudent import HomePageStudent
from Scripts.logOutStudent import LogOutStudent
from Scripts.loginStudent import LoginStudent
from Scripts.inviteURLCSV import GetInviteLink
from Pages.Student.enrollmentPage import EnrollmentPage


@pytest.mark.usefixtures("test_setup")
class TestCreateStudentEnrollmentByInviteLink:

    def test_create_student_account(self):
        driver = self.driver
        self.driver.get(env.URL)
        login_page = LoginPage(driver)
        login_page.click_create_account()
        create_account_page = CreateAccountPage(driver)
        student_email = utils.StudentEmail_2
        create_account_page.input_email(student_email)
        create_account_page.reenter_email_input(student_email)
        create_account_page.click_username()
        create_account_page.clear_username()
        student_user_name = utils.StudentUserName_2
        create_account_page.input_username(student_user_name)
        create_account_page.input_password(env.PASSWORD)
        student_first_name = random.choice(randomNames.first_names)
        create_account_page.input_first_name(student_first_name)
        student_last_name = random.choice(randomNames.last_names)
        create_account_page.input_last_name(student_last_name)
        with open('/Users/vburiol/Documents/AutomationOutput/StudentData.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Student Email', 'Student User Name', 'Password', 'Student First Name',
                             'Student Last Name'])
            writer.writerow([student_email, student_user_name, env.PASSWORD, student_first_name, student_last_name])
        create_account_page.input_country(utils.Country)
        create_account_page.click_return_on_country(Keys.RETURN)
        create_account_page.click_select_role()
        create_account_page.select_role(utils.StudentRole)
        create_account_page.check_agree_terms_of_use()
        create_account_page.click_create_account()
        time.sleep(2)
        try:
            assert create_account_page.get_text_account_created() == "Account created"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("_%m-%d-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                + ".png")
            raise

        except:
            print("There was an exception")
            curr_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S_")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                + ".png")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute")
        create_account_page.click_continue_btn()
        time.sleep(1)
        create_account_page.click_skip_link()
        time.sleep(1)
        create_account_page.yes_skip_link()
        time.sleep(1)
        home_page_student = HomePageStudent(driver)
        try:
            assert home_page_student.not_joined_course_yet() == "You haven't joined your course yet."
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("_%m-%d-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                + ".png")
            raise

        except:
            print("There was an exception")
            curr_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S_")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                + ".png")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute")
        time.sleep(1)
        logout_student = LogOutStudent(driver)
        logout_student.logout_as_student()
        time.sleep(1)

    def test_launch_course_first_time_enrollment_by_invite_link_existing_student(self):
        try:
            driver = self.driver
            invite_link = GetInviteLink(driver)
            driver.get(invite_link.invite_student_link())
            print((invite_link.invite_student_link()))
            enrollment_page = EnrollmentPage(driver)
            enrollment_page.click_get_temporary_access()
            time.sleep(1)
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
            time.sleep(2)
            enrollment_page.text_start_temp_access()
            time.sleep(5)
            home_page_student = HomePageStudent(driver)
            home_page_student.click_course_name()
            assignments_page = AssignmentsPage(driver)
            time.sleep(5)
            i_frame = assignments_page.switch_to_i_frame()
            driver.switch_to.frame(i_frame)
            assert assignments_page.text_pop_up() == "Class with Revel just got easier"
            assignments_page.click_close_class_with_revel_just_got_easier_popup()
            assert home_page_student.get_course_name_home_page() == assignments_page.get_course_name()
            driver.switch_to.default_content()
            time.sleep(1)
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("_%m-%d-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                + ".png")
            raise

        except:
            print("There was an exception")
            curr_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S_")
            test_name = utils.whoami()
            screenshot_name = str(test_name) + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/vburiol/PycharmProjects/GLP_Test/Screenshots/" + screenshot_name
                + ".png")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute")
        # assignments_page.click_close_start_here()
        # time.sleep(2)






