from Pages.Instructor.homePage import HomePage
import time
import csv


class CourseURL:

    def __init__(self, driver):
        self.driver = driver

    def get_course_url(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.click_name_created_course()
        time.sleep(2)
        url_now = driver.current_url  # Course URL
        with open('/Users/vburiol/Documents/AutomationOutput/CourseLink.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Course URL'])
            writer.writerow([url_now])
        return url_now
