"""Test suite for login functionality using pytest and allure reporting."""
import pytest
import allure
from pages.login_page import LoginPage
from utilities.logger import logger

@pytest.fixture(scope="function")
def login_page(driver):
    """Fixture to initialize and return the LoginPage object after navigating to login."""
    page = LoginPage(driver)
    page.navigate_to_login()
    logger.info("Navigated to login page")
    return page

@allure.epic("Authentication")
@allure.feature("Login Functionality")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "regression")
def test_successful_login(login_page):
    """Test that a user can log in successfully with valid credentials."""
    with allure.step("Enter valid credentials"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
    
    with allure.step("Click login button"):
        login_page.click_login()
    
    with allure.step("Verify successful login"):
        assert login_page.is_inventory_page_displayed(), \
            "Inventory page not displayed after login"
        logger.info("Login successful - inventory page displayed")

@allure.story("Failed Login")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression")
@pytest.mark.parametrize(
    "username,password,error_message",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("invalid_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required")
    ]
)
def test_failed_login(login_page, username, password, error_message):
    with allure.step(f"Test invalid login: {username}/{password}"):
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        actual_error = login_page.get_error_message()
        assert error_message in actual_error, f"Expected '{error_message}' but got '{actual_error}'"
        logger.warning("Login failed as expected: %s", actual_error)

@allure.story("Password Masking")
@allure.severity(allure.severity_level.MINOR)
def test_password_masking(login_page):
    """Test that the password field masks the input."""
    with allure.step("Verify password field masks input"):
        login_page.enter_password("secret")
        input_type = login_page.get_password_field_type()
        assert input_type == "password", "Password is not masked"
        logger.info("Password masking verified")