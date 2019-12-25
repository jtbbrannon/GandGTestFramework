from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data.config import settings
from data.config import mappings
from controller.wait_for_frames import wait_for_frames
from webdriver import dr
from controls.button import Button
from controls.textbox import TextBox
from controls.type import ComType
import time

class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def load_website(self):
        dr.get(settings['url'] + "/#" + settings['urlExt'])
        dr.maximize_window()
        if "google.com" in str(dr.current_url).lower():
            webapp.google_login()
        load = dr.find_element_by_id('load')
        if load.is_displayed():
            urlInput = dr.find_element_by_id("url")
            urlInput.clear()
            urlInput.send_keys(settings['urlExt'])
            loadBtn = dr.find_element_by_xpath("//*[@id='load']/form/input[@type='submit']")
            loadBtn.click()

    def refresh_page(self):
        dr.switch_to_default_content()
        refresh = dr.find_element_by_id("refresh_all")
        refresh.click()
    
    def google_login(self):
        un = dr.find_element_by_id("identifierId")
        un.send_keys(settings['UserName'])
        unNextBtn = dr.find_element_by_id("identifierNext")
        unNextBtn.click()
        pw = dr.find_element_by_xpath("//*[@id='password']//input")
        pw.send_keys(settings['Password'])
        wait = WebDriverWait(dr, 10)
        pwNextBtn =wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
        time.sleep(1)
        dr.execute_script("arguments[0].click();", pwNextBtn)


    def switch_to_device(self, device):
        wait = WebDriverWait(dr, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@id, 'controller')]")))
        frames = wait.until(wait_for_frames('iframe', 3))
        frameDevice = frames[device]
        dr.switch_to_frame(frameDevice)
        dr.switch_to_frame("iframe")
        

    def verify_component_exists(self, component):
        button = ComType(component).getObject()
        wait = WebDriverWait(dr, 10)
        wait.until(EC.presence_of_element_located((By.ID, button.locator)))
        value = button.get_value()
        assert component in value, \
            "Component {} not found on page".format(component)

    def verify_component_enablement(self, component, attribute):
        button = ComType(component).getObject()
        if attribute in "enabled":
            assert str(True) in str(button.enabled), \
                "Component {} is disabled".format(component)
        else:
            assert str(False) in str(button.enabled), \
                "Component {} is enabled".format(component)


webapp = WebApp.get_instance()
