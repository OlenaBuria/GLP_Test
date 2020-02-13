from Pages.Instructor.diagnosticManagementPage import DiagnosticManagement
from Pages.Instructor.inviteStudentsPopUp import InviteStudents
from Scripts.courseURL import CourseURL
from Utils import env
import time
import csv


class InviteURL:

    def __init__(self, driver):
        self.driver = driver

    def get_invite_student_url(self):
        driver = self.driver
        course_url = CourseURL(driver)
        get_course_url = course_url.get_course_url()
        self.driver.get(env.HomePageURL)
        # ^^ to fix not existing RIO / can`t locate element for Pearson Logo?? to get invite student flow
        time.sleep(4)
        # diagnostic_management = DiagnosticManagement(driver)
        # time.sleep(1)
        # diagnostic_management.pearson_logo_back_btn_click()
        # time.sleep(2)
        driver.find_element_by_xpath(
            "//div[@class='course-info']"
            "//a[@href=" + " '" + get_course_url + "'" + "]//following-sibling::div[@class='course-options ']//span")\
            .click()
        time.sleep(2)
        invite_students = InviteStudents(driver)
        invite_students.click_copy_link_btn()
        time.sleep(2)
        invite_link = invite_students.get_invite_link()  # Invite Student URL
        with open('/Users/vburiol/Documents/AutomationOutput/InviteLink.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Invite Link'])
            writer.writerow([invite_link])
        time.sleep(1)
        invite_students.click_close_btn()
        time.sleep(3)
        return invite_link
