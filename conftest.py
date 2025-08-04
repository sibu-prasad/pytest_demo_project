import pytest
from utilities.driver_manager import DriverManager
from utilities.logger import logger
import allure

@pytest.fixture(scope="function")
def driver():
    web_driver = DriverManager.get_driver()
    logger.info("Browser launched")
    yield web_driver
    if web_driver:
        web_driver.quit()
        logger.info("Browser closed")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver is not None:
            logger.error(f"Test failed: {item.name}, capturing screenshot")
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )