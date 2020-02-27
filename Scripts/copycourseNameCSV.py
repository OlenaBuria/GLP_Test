import csv


class GetCopyCourseName:

    def __init__(self, driver):
        self.driver = driver

    def get_copy_course_name(self):
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/CopyCourseName.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                course_name = row["Copy Course Name"]
                return course_name
        reader.close()
