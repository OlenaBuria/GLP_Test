import csv


class GetInviteLink:

    def __init__(self, driver):
        self.driver = driver

    def invite_student_link(self):
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/InviteLink.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                invite_link = row["Invite Link"]
                return invite_link
        reader.close()

