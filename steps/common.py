from behave import *
from framework.webapp import webapp

def __init__(self):
        self.driver = webapp.get_driver()

def after_scenario(context, scenario):
    webapp.refresh_page()

def after_feature(context, scenario):
    webapp.close_page()

@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()

@when(u'I switch to device "{device}"')
def step_impl_switch_to_device(context, device):
    webapp.switch_to_device(int(device))
    
@then(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)
    