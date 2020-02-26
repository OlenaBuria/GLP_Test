from Scripts.courseNameCSV import GetCourseName


class AssignmentsPage:

    def __init__(self, driver):
        self.driver = driver
        get_course_name = GetCourseName(driver)
        self.course_name_text_xpath = "//*[contains(text()," + " '" + get_course_name.get_course_name() + "'" + ")]"
        self.class_with_revel_just_got_easier_popup_close_xpath = "//*[@class='appcues-skip']/a"
        self.start_here_popup_xpath = "//div[@class='appcues-actions-right']//[contains(text(), 'Close')]"
        self.start_assignment_btn_xpath = "//*[contains(text(), 'Start assignment')]"
        self.switch_to_i_frame_xpath = "//*[@class= 'appcues--theme--LhGCBdZbIlYP4WZs2jG ontop fullscreen']/iframe"
        self.pop_up_text_xpath = "//*[@class='rich-text']/div/h4"

    def get_course_name(self):
        course_name = self.driver.find_element_by_xpath(self.course_name_text_xpath).text
        return course_name

    def click_close_class_with_revel_just_got_easier_popup(self):
        self.driver.find_element_by_xpath(self.class_with_revel_just_got_easier_popup_close_xpath).click()

    def click_close_start_here(self):
        self.driver.find_element_by_xpath(self.start_here_popup_xpath).click()

    def click_start_assignment(self):
        self.driver.find_element_by_xpath(self.start_assignment_btn_xpath).click()

    def switch_to_i_frame(self):
        elem = self.driver.find_element_by_xpath(self.switch_to_i_frame_xpath)
        return elem

    def text_pop_up(self):
        text_pop_up = self.driver.find_element_by_xpath(self.pop_up_text_xpath).text
        return text_pop_up




