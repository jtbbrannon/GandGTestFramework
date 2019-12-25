from behave import *
from framework.webapp import webapp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from framework.webdriver import dr
from controls.button import Button
from controls.textbox import TextBox
from controls.type import ComType

@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()

@when(u'I switch to device "{device}"')
def step_impl_switch_to_device(context, device):
    webapp.switch_to_device(int(device))

@when(u'I populate "{component}" with "{text}"')
def step_impl_poulate_component(context, component, text):
    com = ComType(component).getObject()
    wait = WebDriverWait(dr, 10)
    inputCom = wait.until(EC.presence_of_element_located((By.ID, com.locator)))
    inputCom.send_keys(text)

@when(u'I click on "{component}"')
def step_impl_click_component(context, component):
    com = ComType(component).getObject()
    wait = WebDriverWait(dr, 10)
    inputCom = wait.until(EC.presence_of_element_located((By.ID, com.locator)))
    dr.execute_script("arguments[0].click();", inputCom)
    
@then(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)
    
@then(u'I see component "{component}" with attribute "{attribute}"')
def step_impl_verify_component_enablement(context, component, attribute):
    webapp.verify_component_exists(component)
    webapp.verify_component_enablement(component, attribute)