# Testing against multiple environments

from Utils import utils as utils

env_url = utils.URL

if env_url == "qa-int":
    URL = "https://console-qa.pearsoned.com"
    USERNAME = "rio_ins_qa_demo_02"
    PASSWORD = "Password11"
    CourseMaterial = "Mango Cake (GLP Silver Book V4)"
elif env_url == "stg":
    URL = "https://console-stg.pearsoned.com"
    USERNAME = "rio_ins_demo_09"
    PASSWORD = "Password1"
    HomePageURL = "https://console-stg.pearsoned.com/console/home"
    CourseMaterial = "STG Mango Cake (GLP Silver Book V4)"
    # CourseMaterial = "STGTDX30_Qns_QUIZ_RIO_CITE_RIOprMODEL" the course doesn't exist anymore
    InviteStudents = "https://console-stg.pearson.com/enrollment/ssgwbv"
    CourseID = "https://rio-stg.pearson.com/i/courses/5e34689ce4b0b8d8a6f28035"
elif env_url == "prod":
    URL_PROD = "https://console.pearson.com"
    USERNAME_PROD = "glp_qe_ins_prod_001"
    PASSWORD_PROD = "Password@11"
elif env_url == "beta-qa":
    URL_BETA = "https://beta-qa.pearson.com/"
    USERNAME_BETA = "rio_ins_qa_demo_02"
    PASSWORD_BETA = "Password11"

