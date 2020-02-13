import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser name e.g.chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="/Users/vburiol/PycharmProjects/GLP_Test/Drivers/chromedriver")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="/Users/vburiol/PycharmProjects/GLP_Test/Drivers/geckodriver")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")