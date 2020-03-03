from Scripts.copyCourseNameCSV import GetCopyCourseName
from Scripts.courseURLCSV import GetCourseURL


class HomePageCopyCourse:

    def __init__(self, driver):
        self.driver = driver
        copy_course_name = GetCopyCourseName(driver)
        copy_course_name_from_csv = copy_course_name.get_copy_course_name()
        self.large_copy_course_title_text_xpath = "//*[contains(text()," + " '" + copy_course_name_from_csv + "'" + ")]"
        course_url = GetCourseURL(driver)
        get_course_url = course_url.get_course_url()
        self.copy_course_xpath = "//div[@class='course-info']//" \
                                 "a[@href=" + " '" + get_course_url + "'" + "]/" \
                                                                            "div[@class=" \
                                                                            "'pe-title pe-title--large course-title']"

    def name_copy_course_text(self):
        name_copy_course = self.driver.find_element_by_xpath(self.large_copy_course_title_text_xpath).text
        return name_copy_course

    def get_text_copy_course(self):
        text_copy_course = self.driver.find_element_by_xpath(self.copy_course_xpath).text
        return text_copy_course
