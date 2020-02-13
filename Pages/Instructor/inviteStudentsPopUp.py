class InviteStudents:

    def __init__(self, driver):
        self.driver = driver
        self.copy_link_btn_css = ".copy-info:nth-child(4) > .pe-btn__primary--btn_xlarge"
        self.link_address_css = "#inviteLink"
        self.close_icon_css = ".modalClose > .pe-icon--remove-sm-24"

    def click_copy_link_btn(self):
        self.driver.find_element_by_css_selector(self.copy_link_btn_css).click()

    def get_invite_link(self):
        invite_link = self.driver.find_element_by_css_selector(self.link_address_css).get_attribute("value")
        return invite_link

    def click_close_btn(self):
        self.driver.find_element_by_css_selector(self.close_icon_css).click()

