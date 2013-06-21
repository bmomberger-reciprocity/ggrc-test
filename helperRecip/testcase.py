import os, sys, re

#import re,sys

#import com.thoughtworks.selenium.


from unittest import TestCase
#from selenium import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time, unittest
import config
                                                                                                                                                                                                                                                                                
#from recip import config



class WebDriverTestCase(TestCase):


   
    def setup(self):
        browser = config.browser
        if browser == "firefox":
            self.profile = webdriver.firefox.firefox_profile.FirefoxProfile()
            self.profile.native_events_enabled
            self.driver = webdriver.Firefox(self.profile)
            self.profile_path = self.profile.path 
        elif browser =="chrome":
            self.driver = webdriver.Chrome('/Users/diana.tzinov/Downloads/chromedriver')   
        #self.profile = webdriver.Firefox.firefox_profile(self).FirefoxProfile
        #self.profile.native_events_enabled
        #self.driver = webdriver.Firefox(self.profile)
        self.base_url =config.url 
        time.sleep(5)
        self.driver.get(self.base_url)  
        self.verificationErrors = []
        
        
    def tearDown(self):
        self.driver.quit()
 