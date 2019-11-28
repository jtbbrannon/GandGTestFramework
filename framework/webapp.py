from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data.config import settings
from data.config import mappings
from urllib.parse import urljoin
from controller.wait_for_frames import wait_for_frames


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
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

    def load_website(self):
        self.driver.get(settings['url'] + "/#" + settings['urlExt'])
        self.driver.maximize_window()
        if "google.com" in str(self.driver.current_url).lower():
            webapp.google_login()
        load = self.driver.find_element_by_id('load')
        if load.is_displayed():
            urlInput = self.driver.find_element_by_id("url")
            urlInput.clear()
            urlInput.send_keys(settings['urlExt'])
            loadBtn = self.driver.find_element_by_xpath("//*[@id='load']/form/input[@type='submit']")
            loadBtn.click()

    def refresh_page(self):
        self.driver.switch_to_default_content()
        refresh = self.driver.find_element_by_id("refresh_all")
        refresh.click()
    
    def close_page(self):
        self.driver.close()

    def google_login(self):
        un = self.driver.find_element_by_id("identifierId")
        un.send_keys(settings['UserName'])
        unNextBtn = self.driver.find_element_by_id("identifierNext")
        unNextBtn.click()
        pw = self.driver.find_element_by_xpath("//*[@id='password']//input")
        pw.send_keys(settings['Password'])
        pwNextBtn = self.driver.find_element_by_id("passwordNext")
        self.driver.execute_script("arguments[0].click();", pwNextBtn)


    def switch_to_device(self, device):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@id, 'controller')]")))
        frames = wait.until(wait_for_frames('iframe', 3))
        frameDevice = frames[device]
        self.driver.switch_to_frame(frameDevice)
        self.driver.switch_to_frame("iframe")
        

    def verify_component_exists(self, component):
        # Simple implementation
        comMap = mappings[component]
        comBY = comMap["by"]
        comLocator = comMap["locator"]
        element = self.driver.find_element_by_id(comLocator)
        value = element.get_attribute("value")
        assert component in value, \
            "Component {} not found on page".format(component)


webapp = WebApp.get_instance()
