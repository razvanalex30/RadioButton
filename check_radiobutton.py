import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from driver_creation import SeleniumLibraryExt

class SelectRadioButton:

    def __init__(self):
        self.dict = None

   
    def retrieve_radiobuttons(self):
        self.driver = SeleniumLibraryExt.create_driver()
        label_dict = dict()
        xpaths = list()
        ids = list()
        form_1 = self.driver.find_elements_by_xpath("//input[@type='radio']")
        for elem in form_1:
            key = elem.get_attribute('id')
            xpath = f"//input[@type='radio'][@id='{key}']"
            xpaths.append(xpath)
            ids.append(key.lower())
        form_2 = self.driver.find_elements_by_xpath("//label[@class]")
        for i in range(len(form_2)):
            label_dict[form_2[i].text] = xpaths[i]
        self.dict = label_dict

    def select_button(self, selection):
        self.driver = SeleniumLibraryExt.create_driver()
        choice = self.driver.find_element_by_xpath(self.dict[selection])
        self.driver.execute_script("arguments[0].click()", choice)
    