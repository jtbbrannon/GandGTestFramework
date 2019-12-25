from data.config import mappings
from controls.button import Button
from controls.textbox import TextBox

class ComType:
    def __init__(self, component):
        comMap = mappings[component]
        self.comType = comMap["type"]
        self.comLoc = comMap["locator"]
    
    def getObject(self):
        if (self.comType == "Button"):
            return Button(self.comLoc)
        elif (self.comType == "TextBox"):
            return TextBox(self.comLoc)
        else:
            raise Exception('Type: ' + self.comType + ' not found')