import pytest
import csv
import time


@pytest.mark.usefixtures("test_setup")
class TestCreateStudentEnrollment:

    def test_create_student_by_link(self):
        driver = self.driver
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/InviteLink.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                driver.get(row["Invite Link"])
        time.sleep(5)
        reader.close()
