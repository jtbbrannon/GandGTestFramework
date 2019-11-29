from behave import *
from framework.webapp import webapp

@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()

@when(u'I switch to device "{device}"')
def step_impl_switch_to_device(context, device):
    webapp.switch_to_device(int(device))
    
@then(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)
    
@then(u'I see component "{component}" with attribute "{attribute}"')
def step_impl_verify_component_enablement(context, component, attribute):
    webapp.verify_component_exists(component)
    webapp.verify_component_enablement(component, attribute)