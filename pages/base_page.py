"""Base page object for Selenium page interactions."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config_reader import ConfigReader
from utilities.logger import logger

class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = int(ConfigReader().get('project', 'timeout'))

    def find_element(self, locator):
        """Finds an element using the given locator and waits until it is visible."""
        logger.info("Finding element: %s", locator)
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Clicks on the element located by the given locator."""
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        """Sends keys to the element located by the given locator."""
        self.find_element(locator).send_keys(text)