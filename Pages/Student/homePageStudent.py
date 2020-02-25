from Scripts.courseNameCSV import GetCourseName


class HomePageStudent:

    def __init__(self, driver):
        self.driver = driver
        self.student_menu_link_css = "#pmui-profile-dropdown-indicator-close"
        self.sign_out_btn_xpath = "//*[contains(text(), 'Sign Out')]"
        get_course_name = GetCourseName(driver)
        self.small_course_title_text_xpath = \
            "//*[contains(text()," + " '" + get_course_name.get_course_name() + "'" + ")]"

    def click_menu_student(self):
        self.driver.find_element_by_css_selector(self.student_menu_link_css).click()

    def click_sign_out(self):
        self.driver.find_element_by_xpath(self.sign_out_btn_xpath).click()

    def click_course_name(self):
        self.driver.find_element_by_xpath(self.small_course_title_text_xpath).click()

    def get_course_name_home_page(self):
        course_name = self.driver.find_element_by_xpath(self.small_course_title_text_xpath).text
        return course_name
