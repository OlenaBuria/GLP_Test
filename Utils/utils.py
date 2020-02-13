# CONSTANTS
import inspect
import moment

URL = "stg"  # beta-qa, stg, prod, qa-int

# Variables - DON`T CHANGE IT!
SectionTitle = "Auto Mango " + moment.now().strftime("%m-%d-%Y_%H-%M")


def whoami():
    return inspect.stack()[1][3]

