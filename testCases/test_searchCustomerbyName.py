import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddnewCustomer import addNewCustomer
from pageObjects.SearchCustomer import searchCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import readConfig


class Test_searchCustomer_005:
    baseurl = readConfig.getApplicationurl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomer_005(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("------------------URL Lanuched------------------------")

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("---------------------Landed on Login page--------------------")

        self.adcust = addNewCustomer(self.driver)
        self.adcust.clickOnCustomerMenu()
        self.adcust.clickOnCustomerMenuItem()

        self.logger.info("--------------------Customer Menu Page--------------------")

        self.srcust = searchCustomer(self.driver)
        self.srcust.sendName("Ramya")
        self.logger.info("--------------------Customer details sent--------------------")
        self.srcust.clickSeach()
        self.logger.info("--------------------Searching option clicked--------------------")

        if self.srcust.searchCustomerbyname("Ramya"):
            assert True
        else:
            self.logger.info("--------------------Customer Searching is failed----------------------")
            assert False

        self.logger.info("--------------------Customer details Searched Successfully--------------------")
        self.driver.close();

