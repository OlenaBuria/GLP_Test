from selenium.webdriver.support.ui import Select


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.input_email_address_text_id = "emailInput"
        self.reenter_email_input_text_id = "reenterEmailInput"
        self.input_username_id = "usernameInput2"
        self.input_password_id = "passwordInput2"
        self.input_first_name_id = "firstNameInput"
        self.input_last_name_id = "lastNameInput"
        self.input_country_id = "countryInput"
        self.select_role_id = "roleSelect"
        self.check_agree_terms_of_use_css = ".pe-form--group:nth-child(12) label"
        self.create_account_btn_id = "createMyAccountButton"
        self.text_account_created_xpath = "//*[contains(text(), 'Account created')]"
        self.continue_btn_id = "mainButton"
        self.skip_link_id = "skipLink"
        self.yes_skip_link_xpath = "//*[contains(text(), 'Yes, skip')]"
        self.yes_start_temp_access_xpath = "//*[contains(text(), 'Yes, start temp access')]"

    def input_email(self, email_address):
        self.driver.find_element_by_id(self.input_email_address_text_id).send_keys(email_address)

    def reenter_email_input(self, reenter_email_address):
        self.driver.find_element_by_id(self.reenter_email_input_text_id).send_keys(reenter_email_address)

    def input_username(self, username):
        self.driver.find_element_by_id(self.input_username_id).send_keys(username)

    def input_password(self, password):
        self.driver.find_element_by_id(self.input_password_id).send_keys(password)

    def input_first_name(self, first_name):
        self.driver.find_element_by_id(self.input_first_name_id).send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element_by_id(self.input_last_name_id).send_keys(last_name)

    def input_country(self, country):
        self.driver.find_element_by_id(self.input_country_id).send_keys(country)

    def click_return_on_country(self, return_btn):
        self.driver.find_element_by_id(self.input_country_id).send_keys(return_btn)

    def click_select_role(self):
        self.driver.find_element_by_id(self.select_role_id).click()

    def select_role(self, role):
        select = Select(self.driver.find_element_by_id(self.select_role_id))
        select.select_by_visible_text(role)
        return role

    def check_agree_terms_of_use(self):
        self.driver.find_element_by_css_selector(self.check_agree_terms_of_use_css).click()

    def click_create_account(self):
        self.driver.find_element_by_id(self.create_account_btn_id).click()

    def get_text_account_created(self):
        account_created = self.driver.find_element_by_xpath(self.text_account_created_xpath).text
        return account_created

    def click_continue_btn(self):
        self.driver.find_element_by_id(self.continue_btn_id).click()

    def click_skip_link(self):
        self.driver.find_element_by_id(self.skip_link_id).click()

    def yes_skip_link(self):
        self.driver.find_element_by_xpath(self.yes_skip_link_xpath).click()

    def yes_start_temp_access(self):
        self.driver.find_element_by_xpath(self.yes_start_temp_access_xpath).click()




