class HomePageStudent:

    def __init__(self, driver):
        self.driver = driver
        self.student_menu_link_css = "#pmui-profile-dropdown-indicator-close"
        self.sign_out_btn_xpath = "//*[contains(text(), 'Sign Out')]"

    def click_menu_student(self):
        self.driver.find_element_by_css_selector(self.student_menu_link_css).click()

    def click_sign_out(self):
        self.driver.find_element_by_xpath(self.sign_out_btn_xpath).click()
