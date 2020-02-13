class DiagnosticManagement:

    def __init__(self, driver):
        self.driver = driver
        self.pearson_logo_back_btn_xpath = "//dev[@id='pearson-logo-white']"
        self.pearson_logo_back_btn_css = ".pearson-logo"
        self.pearson_logo_back_btn_id = "pearson-logo-white"
        self.diagnostic_locked_text_css = '.large-lbl-b'

    def pearson_logo_back_btn_click(self):
        self.driver.find_element_by_xpath(self.pearson_logo_back_btn_xpath).click()
        # self.driver.find_element_by_css_selector(self.pearson_logo_back_btn_css).click()

    def text_diagnostic_locked(self):
        diagnostic_locked = self.driver.find_element_by_css_selector(self.diagnostic_locked_text_css).text
        return diagnostic_locked
