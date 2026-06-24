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