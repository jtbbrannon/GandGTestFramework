from framework.webdriver import dr

class TextBox:
    def __init__(self, locator):
        self.locator = locator
        self.enabled = self.is_enabled()

    def is_enabled(self):
        element = dr.find_element_by_id(self.locator)
        return element.is_enabled()

    def get_value(self):
        element = dr.find_element_by_id(self.locator)
        return element.get_attribute("placeholder")
    