class ExchangePage:

    def __init__(self, driver):
        self.driver = driver
        self.input_section_title_text_id = "sectionTitleInput"
        self.click_next_btn_id = "submit-bottom"
        self.input_section_code_text_id = "course-section"
        self.online_course_checkbox_id = "online-only-checkbox"
        self.course_start_date_id = "course-start-date"
        self.select_current_date_box_css = ".currentDate-box"
        self.course_end_date_id = "course-end-date"
        self.click_next_calendar_css = ".pe-arrowIcons:nth-child(3)"
        self.select_28day_calendar_id = "day28"
        self.copy_course_name_xpath = "//*[@class='course-name pe-title--large']"
        self.edit_copy_course_xpath = "//*[@class='pe-icon--btn section-tooltip']"

    def click_section_title(self):
        self.driver.find_element_by_id(self.input_section_title_text_id).click()

    def input_section_title(self, section_title):
        self.driver.find_element_by_id(self.input_section_title_text_id).send_keys(section_title)

    def click_next(self):
        self.driver.find_element_by_id(self.click_next_btn_id).click()

    def click_section_code(self):
        self.driver.find_element_by_id(self.input_section_code_text_id).click()

    def input_section_code(self, section_code):
        self.driver.find_element_by_id(self.input_section_code_text_id).send_keys(section_code)

    def check_online_course(self):
        self.driver.find_element_by_id(self.online_course_checkbox_id).click()

    def click_course_start_date(self):
        self.driver.find_element_by_id(self.course_start_date_id).click()

    def click_course_end_date(self):
        self.driver.find_element_by_id(self.course_end_date_id).click()

    def select_current_date_box(self):
        self.driver.find_element_by_css_selector(self.select_current_date_box_css).click()

    def click_next_calendar(self):
        self.driver.find_element_by_css_selector(self.click_next_calendar_css).click()

    def select_28day_calendar(self):
        self.driver.find_element_by_id(self.select_28day_calendar_id).click()

    def click_save(self):
        self.driver.find_element_by_id(self.click_next_btn_id).click()

    def text_copy_course_name_xpath(self):
        copy_course_name_text = self.driver.find_element_by_xpath(self.copy_course_name_xpath).text
        edit_copy_course_text = self.driver.find_element_by_xpath(self.edit_copy_course_xpath).text
        copy_course_needed_text = copy_course_name_text.replace(edit_copy_course_text, '')
        elem_to_extract = "\n"
        copy_course_needed_text_completed = copy_course_needed_text.replace(elem_to_extract, '')
        return copy_course_needed_text_completed




