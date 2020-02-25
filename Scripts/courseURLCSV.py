import csv


class GetCourseURL:

    def __init__(self, driver):
        self.driver = driver

    def get_course_url(self):
        reader = csv.DictReader(open('/Users/vburiol/Documents/AutomationOutput/CourseLink.csv'))
        idx = 0
        for row in reader:
            idx += 1
            if idx == 1:
                course_name = row["Course URL"]
                return course_name
        reader.close()
