import pytest
from Scripts import activate_this
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage # is used to access the file
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl=readConfig.getApplicationurl()
    username=readConfig.getUsername()
    password=readConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def testPageTitle(self,setup):
        self.logger.info("************************TestPageTitle*************************************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************************Login Page Pass*************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"testPageTitle.png")
            self.driver.close()
            self.logger.error("************************Login Page Fail*************************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def testLogin(self,setup):
        self.logger.info("************************ Verifying Login Success*************************************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10) # it waits for 10 secs
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************************Login Success*************************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testLogin.png")
            self.logger.error("************************Login Failure*************************************")
            self.driver.close()
            assert False