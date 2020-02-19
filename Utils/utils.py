# CONSTANTS
import inspect
import moment

URL = "stg"  # beta-qa, stg, prod, qa-int
NumberStudentsToCreate = 2

# Variables - DON`T CHANGE IT!
SectionTitle = "Auto Mango " + moment.now().strftime("%m-%d-%Y_%H-%M")
StudentEmail = "Ol_" + moment.now().strftime("%m.%d.%Y_%H.%M.%S") + "@t.com"
StudentUserName = "Ol_" + moment.now().strftime("%m.%d_%H.%M.%S")
Country = "United States"
StudentRole = "Student"


def whoami():
    return inspect.stack()[1][3]

