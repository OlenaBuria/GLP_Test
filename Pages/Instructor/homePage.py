class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.instructor_menu_link_css = ".o-app-header__username"
        self.my_account_settings_menu_link_css = ".o-app-header__menu-item-my-account > .o-app-header--truncate"
        self.menu_username_displayed_text_id = "displayedUsername"
        self.logout_link_text_css = ".pe-btn__primary--btn_xlarge"

    def click_menu_instructor(self):
        self.driver.find_element_by_css_selector(self.instructor_menu_link_css).click()

    def click_account_settings(self):
        self.driver.find_element_by_css_selector(self.my_account_settings_menu_link_css).click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(self.logout_link_text_css).click()

