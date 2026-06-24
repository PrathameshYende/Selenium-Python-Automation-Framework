from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge(
        service=Service(
            EdgeChromiumDriverManager().install()
        )
    )

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        driver.save_screenshot(
            f"screenshots/{item.name}.png"
        )
