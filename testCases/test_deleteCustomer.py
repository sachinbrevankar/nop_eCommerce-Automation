import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddnewCustomer import addNewCustomer
from pageObjects.SearchCustomer import searchCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
from pageObjects.EditCustomer import editCustomer

class Test_deleteCustomer_TC006:
    baseurl = readConfig.getApplicationurl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()

    def test_deleteCustomer_006(self,setup):
        self.driver =setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("----------------------Launching Browser------------------")

        self.lp= LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("----------------------Landed on Logged In Page--------------------")

        self.adcust = addNewCustomer(self.driver)
        self.adcust.clickOnCustomerMenu()
        self.adcust.clickOnCustomerMenuItem()
        self.logger.info("----------------------Landed on customer details Page---------------------")

        self.srcus = searchCustomer(self.driver)
        self.srcus.sendEmail("eh13jfrs@gmail.com")
        self.srcus.clickSeach()
        self.logger.info("----------------------Searching Customer Details--------------------")
        time.sleep(2)

        self.edt = editCustomer(self.driver)
        self.edt.clickdedit()
        self.logger.info("----------------------Clicked Edit Option--------------------")
        act_title = self.driver.title
        if act_title == "Edit customer details / nopCommerce administration":
            assert True
            self.logger.info("************************Landed on Edit Customer Details Page*************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "editpagedetails.png")
            self.logger.error("************************Landing on edit customer page failure*************************************")
            assert False

        time.sleep(3)

        if self.edt.searched_email("eh13jfrs@gmail.com"):
            self.logger.info("---------- Customer Searched & Matched ----------")
            assert True
        else:
            self.logger.info("---------- Customer Details Mismatching ----------")
            assert False

        self.edt.clickdlt()
        self.logger.info("----------------------Clicked Delete Button---------------------------")
        time.sleep(2)
        self.edt.clickdelete()
        self.logger.info("----------------------Clicked Delete another Btn---------------------")
        time.sleep(2)

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'The customer has been deleted successfully.' in self.msg:
            self.logger.info("---------Successfully deleted the Customer-------------")
            assert True == True
        else:
            self.logger.info("--------Not deleted the customer (Failed)-------------")
            self.driver.save_screenshot("\\Screenshot" + "deleteCustomer.png")
            assert True == False

        self.logger.info("----------------------Delete Customer TC Passed------------------------")
        time.sleep(2)
        self.driver.close()




