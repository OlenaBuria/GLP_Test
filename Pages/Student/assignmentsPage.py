from Scripts.courseNameCSV import GetCourseName


class AssignmentsPage:

    def __init__(self, driver):
        self.driver = driver
        get_course_name = GetCourseName(driver)
        self.course_name_text_xpath = "//*[contains(text()," + " '" + get_course_name.get_course_name() + "'" + ")]"
        self.class_with_revel_just_got_easier_popup_close_xpath = "//div[@class='appcues-skip']a[contains(text(), 'x')]"
        self.class_with_revel_just_got_easier_popup_close_link = "x"

        self.start_here_popup_xpath = "//div[@class='appcues-actions-right']//[contains(text(), 'Close')]"
        self.start_assignment_btn_xpath = "//*[contains(text(), 'Start assignment')]"

    def get_course_name(self):
        course_name = self.driver.find_element_by_xpath(self.course_name_text_xpath).text
        return course_name

    def click_close_class_with_revel_just_got_easier_popup(self):
        self.driver.find_element_by_xpath(self.class_with_revel_just_got_easier_popup_close_xpath).click()
        # self.driver.find_element_by_link_text(self.class_with_revel_just_got_easier_popup_close_link).click()

    def click_close_start_here(self):
        self.driver.find_element_by_xpath(self.start_here_popup_xpath).click()

    def click_start_assignment(self):
        self.driver.find_element_by_xpath(self.start_assignment_btn_xpath).click()


