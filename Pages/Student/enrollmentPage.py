class EnrollmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_365_temporary_access_btn_xpath = "//*[contains(text(), 'Get 365-day temporary access')]"
        self.start_temp_access_xpath = "//*[contains(text(), 'Yes, start temp access')]"

    def click_get_temporary_access(self):
        self.driver.find_element_by_xpath(self.get_365_temporary_access_btn_xpath).click()

    def text_start_temp_access(self):
        self.driver.find_element_by_xpath(self.start_temp_access_xpath).click()
