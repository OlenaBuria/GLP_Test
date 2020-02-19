import time
import pytest
from Scripts.newStudentsAccounts import NewStudentsAccounts
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestCreateNumberOfStudents:

    def test_create_multiple_students(self):
        for i in range(0, utils.NumberStudentsToCreate):
            new_students_accounts = NewStudentsAccounts(self.driver)
            new_students_accounts.create_new_students_accounts()
            time.sleep(2)


