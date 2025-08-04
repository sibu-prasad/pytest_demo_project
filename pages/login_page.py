from .base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.config_reader import ConfigReader

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.config = ConfigReader()
    
    def navigate_to_login(self):
        base_url = self.config.get('project', 'base_url')
        self.driver.get(base_url)
        self.find_element(self.USERNAME_INPUT)

    def enter_username(self, username):
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def is_inventory_page_displayed(self):
        return self.is_element_displayed(self.INVENTORY_CONTAINER)

    def is_element_displayed(self, locator):
        from selenium.common.exceptions import NoSuchElementException
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def get_password_field_type(self):
        return self.find_element(self.PASSWORD_INPUT).get_attribute("type")