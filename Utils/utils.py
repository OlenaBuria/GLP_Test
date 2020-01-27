#CONSTANTS
import inspect

URL = "https://rio-qa.pearson.com/"
USERNAME = "rio_ins_qa_demo_02"
PASSWORD = "Password11"


def whoami():
    return inspect.stack()[1][3]