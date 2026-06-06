import pytest
import time

from selenium.webdriver.common.by import By

tablerow_xpath= "//table[@id='customers-grid']//tbody/tr"
btnedit_xpath="//a[normalize-space()='Edit']"
txtemail_id="Email"
btndelete1_xpath= "//span[@id='customer-delete']"
btndelete2_xpath= "//button[normalize-space()='Delete']"


class editCustomer():
    def __init__(self, driver):
        self.driver = driver

    def clickdedit(self):
        editbtn = self.driver.find_element(By.XPATH,"//table//tr/td[7]")
        editbtn.click()

    def searched_email(self, srcname):
        namebox = self.driver.find_element(By.ID,txtemail_id).get_attribute("value")
        return namebox == srcname

    def clickdlt(self):
        self.driver.find_element(By.XPATH, btndelete1_xpath).click()

    def clickdelete(self):
        self.driver.find_element(By.XPATH, btndelete2_xpath).click()


