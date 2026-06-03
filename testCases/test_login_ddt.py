import time

import pytest
from Scripts import activate_this
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage # is used to access the file
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
from utilities.XLUtils import XLUtils

class Test_002_DDT_Login:
    baseurl=readConfig.getApplicationurl()
    path=".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def testLogin_ddt(self,setup):
        self.logger.info("************************DDT Test Case**************************")
        self.logger.info("************************ Verifying Login Success*************************************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)

        self.row=XLUtils.getRowCount(self.path,'Sheet1')
        print("The num of rows:",self.row)

        lst_status=[]  # Empty List array to store the Status

        for r in range(2,self.row+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("******************TC DDT Passed********************")
                    self.lp.clickLogout()
                    time.sleep(2)
                    self.driver.get(self.baseurl)

                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*******************TC DDT Failed*********************")
                    self.lp.clickLogout()
                    time.sleep(2)
                    self.driver.get(self.baseurl)
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("******************TC DDT Failed********************")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*******************TC DDT Passed*********************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********************Login DDT TC is Passed***********************")
            self.driver.close()
            assert True
        else:
            self.logger.info("********************Login DDT TC is Failed**************************")
            self.driver.close()
            assert False

        self.logger.info("----End of the Login DDT Testcase----")
        self.logger.info("----Completed Login DDT TC002----")


