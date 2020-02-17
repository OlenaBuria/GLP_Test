import pytest
import csv
import time
import random
import moment
import allure
from Pages.Student.enrollmentPage import EnrollmentPage
from Pages.Instructor.loginPage import LoginPage
from Pages.Student.createAccountPage import CreateAccountPage
from Utils import utils as utils
from Utils import env
from selenium.webdriver.common.keys import Keys
from Utils import randomNames as randomNames


@pytest.mark.usefixtures("test_setup")
class TestCreateStudentEnrollment:

    def test_create_student_by_link(self):
        for i in range(utils.NumberStudentsToCreate):
            driver = self.driver
            reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/InviteLink.csv'))
            idx = 0
            for row in reader:
                idx += 1
                if idx == 1:
                    driver.get(row["Invite Link"])
            time.sleep(5)
            reader.close()
            enrollment_page = EnrollmentPage(driver)
            enrollment_page.click_get_temporary_access()
            login_page = LoginPage(driver)
            login_page.click_create_account()
            create_account_page = CreateAccountPage(driver)
            student_email = utils.StudentEmail
            create_account_page.input_email(student_email)
            create_account_page.reenter_email_input(student_email)
            student_user_name = utils.StudentUserName
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
            time.sleep(5)
            create_account_page.yes_start_temp_access()
            time.sleep(3)



