'''
Created on Jul 24, 2013

@author: diana.tzinov
'''


import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers


class TestProductCreate(WebDriverTestCase):
    
    
    def testProductCreate(self):
        self.testname="testProductCreate"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers()
        do.setUtils(util)
        do.Login()
        last_created_object_link =do.CreateObject("Product")
        do.NavigateToObjectAndOpenObjectEditWindow("Product",last_created_object_link)
        do.deleteObject()
 
        
        
if __name__ == "__main__":
    unittest.main()