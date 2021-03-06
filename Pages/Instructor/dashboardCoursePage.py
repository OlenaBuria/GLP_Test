class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.encourage_reading_text_css = ".pe-bold > span"
        self.create_assignment_btn_css = ".imitation-pe-btn-primary > span"
        self.popup_success_published_assignment_css = ".pe-label"
        self.popup_success_published_assignment_xpath = "//div[@class='alert-content']"
        self.success_popup_close_icon_css = ".close-title"
        self.course_name_course_page_tag_name = "h1"

    def no_assignments_yet(self):
        encourage_reading_text = self.driver.find_element_by_css_selector(self.encourage_reading_text_css).text
        return encourage_reading_text

    def click_create_assignment(self):
        self.driver.find_element_by_css_selector(self.create_assignment_btn_css).click()

    def success_popup_published_assignment(self):
        success_popup = self.driver.find_element_by_xpath(self.popup_success_published_assignment_xpath).text
        return success_popup

    def click_close_icon_on_success_popup(self):
        self.driver.find_element_by_css_selector(self.success_popup_close_icon_css).click()

    def get_text_course_name(self):
        course_name_course_page = self.driver.find_element_by_tag_name(self.course_name_course_page_tag_name).text
        return course_name_course_page




