from Pages.Instructor.exchangePage import ExchangePage
import csv


class CopyCourseName:

    def __init__(self, driver):
        self.driver = driver

    def get_copy_course_name(self):
        driver = self.driver
        exchange_page = ExchangePage(driver)
        name_copy_course = exchange_page.text_copy_course_name_xpath()
        with open('/Users/vburiol/Documents/AutomationOutput/CopyCourseName.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Copy Course Name'])
            writer.writerow([name_copy_course])
        return name_copy_course
