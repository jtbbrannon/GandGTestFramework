from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data.config import settings

class wait_for_frames(object):

  def __init__(self, tag_name, number_of_frames):
    self.tag_name = tag_name
    self.number_of_frames = number_of_frames - 1

  def __call__(self, driver):
    frames = driver.find_elements_by_tag_name(self.tag_name)
    if len(frames) > self.number_of_frames:
        return frames
    else:
        return False