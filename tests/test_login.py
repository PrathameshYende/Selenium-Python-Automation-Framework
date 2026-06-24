from pages.login_page import LoginPage
import time

def test_login(driver):

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    login = LoginPage(driver)
    time.sleep(2)

    login.enter_username("standard_user")
    time.sleep(2)
    login.enter_password("secret_sauce")
    time.sleep(2)
    login.click_login()
    time.sleep(2)

    assert "inventory" in driver.current_url