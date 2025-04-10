

import pytest
import datetime
import os
from selenium import webdriver
from TDD.config.test_config import Test_Config

@pytest.fixture
def driver():
    browser = Test_Config.browser_name
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":  # Fixed casing for Firefox
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()


def pytest_configure(config):
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_dir = f"../reports/allure_report/report_{timestamp}"
        os.makedirs(report_dir, exist_ok=True)
        config.option.allure_report_dir = report_dir
        report_file = f"../reports/report_{timestamp}.html"
        config.option.htmlpath = report_file
    except Exception as e:
        print(str(e))