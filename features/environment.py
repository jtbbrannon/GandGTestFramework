from behave import *
from framework.webapp import webapp
from framework.webdriver import driver

def after_scenario(context, scenario):
    webapp.refresh_page()

def after_feature(context, scenario):
    driver.close_page()