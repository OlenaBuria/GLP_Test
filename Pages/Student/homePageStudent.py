from Scripts.courseNameCSV import GetCourseName


class HomePageStudent:

    def __init__(self, driver):
        self.driver = driver
        self.student_menu_link_css = "#pmui-profile-dropdown-indicator-close"
        self.sign_out_btn_xpath = "//*[contains(text(), 'Sign Out')]"
        get_course_name = GetCourseName(driver)
        self.small_course_title_text_xpath = \
            "//*[contains(text()," + " '" + get_course_name.get_course_name() + "'" + ")]"
        self.account_settings_menu_css = ".applyHover > span"
        self.displayed_user_name_menu_id = "displayedUsername"
        self.not_joined_course_yet_xpath = "//*[@class='placeholder-content']/h3"

    def click_menu_student(self):
        self.driver.find_element_by_css_selector(self.student_menu_link_css).click()

    def click_account_settings_menu(self):
        self.driver.find_element_by_css_selector(self.account_settings_menu_css).click()

    def displayed_user_name_menu(self):
        displayed_user_name_menu = self.driver.find_element_by_id(self.displayed_user_name_menu_id).text
        return displayed_user_name_menu

    def click_sign_out(self):
        self.driver.find_element_by_xpath(self.sign_out_btn_xpath).click()

    def click_course_name(self):
        self.driver.find_element_by_xpath(self.small_course_title_text_xpath).click()

    def get_course_name_home_page(self):
        course_name = self.driver.find_element_by_xpath(self.small_course_title_text_xpath).text
        return course_name

    def not_joined_course_yet(self):
        not_joined_course_yet = self.driver.find_element_by_xpath(self.not_joined_course_yet_xpath).text
        return not_joined_course_yet
