# CONSTANTS
import inspect
import moment

URL = "stg"  # beta-qa, stg, prod, qa-int
NumberStudentsToCreate = 1

# Variables - DON`T CHANGE IT!
SectionTitle = "Auto Mango " + moment.now().strftime("%m-%d-%Y_%H-%M")
StudentEmail = "Olena_" + moment.now().strftime("%m.%d.%Y_%H.%M") + "@test.com"
StudentUserName = "Olena_" + moment.now().strftime("%m.%d.%Y_%H.%M")
Country = "United States"
StudentRole = "Student"



def whoami():
    return inspect.stack()[1][3]

