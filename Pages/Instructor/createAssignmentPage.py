class CreateAssignmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.chapter1_section_btn_css = ".rst__node:nth-child(2) .pe-link"
        self.chapter1_section_btn_xpath = "//*[contains(text(), 'Chapter 1: The Principles and" \
                                          " Practice of Economics:Select to Expand')]"
        self.select_all_check_box_css = ".select-all-checkbox"
        self.select_all_check_box_xpath = "//div[@class='circleCheckBox circle-check  ']"
        self.add_content_btn_css = "#toc-header-add-button"
        self.publish_btn_css = "#assignment-publish-button > span"
        self.due_date_calendar_css = "#ahc-datePicker"
        self.next_arrow_calendar_css = ".pe-icon--chevron-next-18"
        self.date_day28_calendar_css = "#day28"

    def click_chapter1(self):
        self.driver.find_element_by_css_selector(self.chapter1_section_btn_css).click()

    def click_select_all(self):
        self.driver.find_element_by_xpath(self.select_all_check_box_xpath).click()

    def click_add_content(self):
        self.driver.find_element_by_css_selector(self.add_content_btn_css).click()

    def click_publish_assignment(self):
        self.driver.find_element_by_css_selector(self.publish_btn_css).click()

    def click_due_date(self):
        self.driver.find_element_by_css_selector(self.due_date_calendar_css).click()

    def click_next_month(self):
        self.driver.find_element_by_css_selector(self.next_arrow_calendar_css).click()

    def select_day28_calendar(self):
        self.driver.find_element_by_css_selector(self.date_day28_calendar_css).click()



