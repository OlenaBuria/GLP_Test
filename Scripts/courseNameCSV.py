import csv


class GetCourseName:

    def __init__(self, driver):
        self.driver = driver

    def get_course_name(self):
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/CourseName.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                course_name = row["Course Name"]
                return course_name
        reader.close()
