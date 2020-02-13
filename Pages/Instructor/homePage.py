from Utils import utils as utils


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.instructor_menu_link_css = ".o-app-header__username"
        self.my_account_settings_menu_link_css = ".o-app-header__menu-item-my-account > .o-app-header--truncate"
        self.menu_username_displayed_text_id = "displayedUsername"
        self.logout_link_text_css = ".pe-btn__primary--btn_xlarge"
        self.got_it_popup_link_css = ".o-coach-mark__got-it"
        self.large_course_title_text_xpath = "//*[contains(text()," + " '" + utils.SectionTitle + "'" + ")]"

    def click_menu_instructor(self):
        self.driver.find_element_by_css_selector(self.instructor_menu_link_css).click()

    def click_account_settings(self):
        self.driver.find_element_by_css_selector(self.my_account_settings_menu_link_css).click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(self.logout_link_text_css).click()

    def click_link_got_it(self):
        self.driver.find_element_by_css_selector(self.got_it_popup_link_css).click()

    def name_created_course_text(self):
        name_course = self.driver.find_element_by_xpath(self.large_course_title_text_xpath).text
        return name_course

    def click_name_created_course(self):
        self.driver.find_element_by_xpath(self.large_course_title_text_xpath).click()

