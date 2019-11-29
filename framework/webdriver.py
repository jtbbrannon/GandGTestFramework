from selenium import webdriver
from data.config import settings

class WebDriver:
    instance = None
    driver = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebDriver()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(30)
        else:
            self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def close_page(self):
        self.driver.close()

driver = WebDriver.get_instance()
dr = driver.get_driver()