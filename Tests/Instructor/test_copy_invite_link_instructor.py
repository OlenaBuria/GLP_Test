import pytest
import time
from Scripts.loginInstructor import LoginInstructor
from Scripts.inviteURL import InviteURL


@pytest.mark.usefixtures("test_setup")
class TestCopyInviteLink:

    def test_copy_course_invite_link_from_home_page_instructor(self):
        driver = self.driver
        login_instructor = LoginInstructor(driver)
        login_instructor.login_as_instructor()
        invite_url = InviteURL(driver)
        invite_link = invite_url.get_invite_student_url()
        driver.execute_script("window.open('" + invite_link + "');")
        time.sleep(1)