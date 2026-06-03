import string
import random
import pytest
import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
from pageObjects.AddnewCustomer import addNewCustomer
from selenium.webdriver.common.by import By

class Test_003_AddCustomer():
    baseurl = readConfig.getApplicationurl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer_003(self,setup):
        self.logger.info("------------TC003 Add New Customer--------------------")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("------------Login Successful-------------------")

        self.addcust = addNewCustomer(self.driver)

        self.addcust.clickOnCustomerMenu()
        self.logger.info("------------Customer Click is working---------------------")
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("------------Sending Customer details---------------------")

        self.email = random_gen() +"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test1234")
        self.fname = random_fname()
        self.lname = random_lname()
        self.addcust.setFirstName(self.fname)
        self.addcust.setLastName(self.lname)
        self.addcust.setGender("Female")
        self.addcust.setCompany( self.fname + " Avenue")
        self.addcust.setIsTaxExempt()
        self.addcust.setCompanyRole("Vendors")
        #self.addcust.setMangerVendor("Vendor 2")
        #self.addcust.activeRd()
        self.addcust.setAdminContent("This is for Python Script Testing......!")
        self.addcust.cLickOnSave()

        self.logger.info("------------Saving Customer details---------------------")
        self.logger.info("-------Add Customer Validation started---------")

        self.msg= self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            self.logger.info("---------Successfully added new customer details-------------")
            assert True == True
        else:
            self.logger.info("--------Not added new customer details(Failed)-------------")
            self.driver.save_screenshot("\\Screenshot" + "testAddnew_scr.png")
            assert True == False

        self.driver.close()
        self.logger.info("---------Closing Add customer page---------")

def random_gen(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_fname(size=6,chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size)).capitalize()

def random_lname(size=2,chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size)).upper()