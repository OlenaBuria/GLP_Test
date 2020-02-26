from Utils import utils as utils
from Scripts.courseURLCSV import GetCourseURL


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.instructor_menu_link_css = ".o-app-header__username"
        self.my_account_settings_menu_link_css = ".o-app-header__menu-item-my-account > .o-app-header--truncate"
        self.menu_username_displayed_text_id = "displayedUsername"
        self.logout_link_text_css = ".pe-btn__primary--btn_xlarge"
        self.got_it_popup_link_css = ".o-coach-mark__got-it"
        self.large_course_title_text_xpath = "//*[contains(text()," + " '" + utils.SectionTitle + "'" + ")]"
        course_url = GetCourseURL(driver)
        get_course_url = course_url.get_course_url()
        self.course_options_xpath = "//div[@class='course-info']//" \
                                    "a[@href=" + " '" + get_course_url + "'" + "]//" \
                                                                               "following-sibling::" \
                                                                               "div[@class='course-options ']//" \
                                                                               "*[contains(text(), 'Course Options')]"
        self.copy_course_xpath = "//div[@class='course-info']//" \
                                 "a[@href=" + " '" + get_course_url + "'" + "]//" \
                                                                            "following-sibling::" \
                                                                            "div[@class='course-options ']//" \
                                                                            "*[contains(text(), 'Copy Course')]"
        self.coach_mark_title_got_it_xpath = "//div[@class='o-coach-mark__content ']/h6"

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

    def click_course_options(self):
        self.driver.find_element_by_xpath(self.course_options_xpath).click()

    def click_copy_course(self):
        self.driver.find_element_by_xpath(self.copy_course_xpath).click()

    def coach_mark_title(self):
        coach_mark_title = self.driver.find_element_by_xpath(self.coach_mark_title_got_it_xpath).text
        return coach_mark_title


