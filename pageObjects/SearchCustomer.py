import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


class searchCustomer:

    txtemail_xpath = "//input[@id='SearchEmail']"
    txtname_xpath ="//input[@id='SearchFirstName']"
    btnsearch_xpath ="//button[@id='search-customers']"
    cuttable_xpath="//table[@id='customers-grid']"
    tablerow_xpath= "//table[@id='customers-grid']//tbody/tr"
    tablecol_xpath= "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver = driver

    def sendEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtemail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtemail_xpath).send_keys(email)

    def sendName(self,cusname):
        self.driver.find_element(By.XPATH, self.txtname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtname_xpath).send_keys(cusname)

    def clickSeach(self):
        self.driver.find_element(By.XPATH,self.btnsearch_xpath).click()

    def searchCustomerbyemail(self, email):
        rows = self.driver.find_elements(By.XPATH, self.tablerow_xpath)
        for row in rows:
            custemail = row.find_element(By.XPATH, "./td[2]").text.strip()
            print("Email Found:", custemail)
            if custemail.lower() == email.lower():
                return True
        return False

    def searchCustomerbyname(self, cusname):
        rows = self.driver.find_elements(By.XPATH, self.tablerow_xpath)
        for row in rows:
            custname = row.find_element(By.XPATH, "./td[3]").text.strip()
            print("Name Found:", custname)
            if cusname.lower() in custname.split()[0].lower(): # Split by space and take the first item
                return True
        return False
