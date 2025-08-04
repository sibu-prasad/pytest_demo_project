from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.config_reader import ConfigReader

class DriverManager:
    @staticmethod
    def get_driver():
        config = ConfigReader()
        browser = config.get('project', 'browser').lower()
        headless = config.get('project', 'headless').lower() == 'true'

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        return driver