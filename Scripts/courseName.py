import csv
from Pages.Instructor.homePage import HomePage


class GetCourseName:

    def __init__(self, driver):
        self.driver = driver

    def get_course_name(self):
        driver = self.driver
        exchange_page = HomePage(driver)
        course_name = exchange_page.name_created_course_text()
        with open('/Users/vburiol/Documents/AutomationOutput/CopyCourseName.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Copy Course Name'])
            writer.writerow([course_name])
        return course_name
