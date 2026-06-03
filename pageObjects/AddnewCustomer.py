import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys

class addNewCustomer:
    rdclose_xpath ="//button[contains(text(),'×')]"
    lnkcustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkcustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnaddnew_xpath = "//a[normalize-space()='Add new']"
    txtemail_xpath = "//input[@id='Email']"
    txtpassword_xpath = "//input[@id='Password']"
    txtfrtname_xpath = "//input[@id='FirstName']"
    txtlstname_xpath = "//input[@id='LastName']"
    rdtgenderM_id = "Gender_Male"
    rdtgenderF_id = "Gender_Female"
    txtcmpname_xpath = "//input[@id='Company']"
    rdtax_id = "IsTaxExempt"
    txtcustomerrole_xpath = "//input[@role='searchbox']"
    lstadmrole_xpath = "//li[contains(text(),'Administrators')]"
    lstfmoderator_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstregister_xpath = "//li[contains(text(),'Registered')]"
    lstguest_xpath = "//li[contains(text(),'Guests')]"
    lstvendor_xpath = "//li[contains(text(),'Vendors')]"
    rmvcrs_xpath ="//span[@role='presentation'][normalize-space()='×']"
    txtmanvendors_xpath = "//span[@id='select2-VendorId-container']"
    #lstnotvendor_xpath = "//li[@id='select2-VendorId-result-hpkr-0']"
    #lstvendor1_xpath = "//li[@id='select2-VendorId-result-ynzi-1']"
    #lstvendor2_xpath = "//li[@id='select2-VendorId-result-i6os-2']"
    rdactive_id ="Active"
    rdchangepswd_id ="MustChangePassword"
    txtcustcomment_xpath="//textarea[@id='AdminComment']"
    btnsave_xpath ="//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickXbtn(self):
        self.driver.find_element(By.XPATH,self.rdclose_xpath).click()

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkcustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnaddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtemail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtpassword_xpath).send_keys(password)

    def setFirstName(self,firstName):
        self.driver.find_element(By.XPATH,self.txtfrtname_xpath).send_keys(firstName)

    def setLastName(self,lastName):
        self.driver.find_element(By.XPATH,self.txtlstname_xpath).send_keys(lastName)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdtgenderM_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rdtgenderF_id).click()
        else:
            self.driver.find_element(By.ID,self.rdtgenderM_id).click()

    def setCompany(self,company):
        self.driver.find_element(By.XPATH,self.txtcmpname_xpath).send_keys(company)

    def setIsTaxExempt(self):
        self.driver.find_element(By.ID, self.rdtax_id).click()

    def setCompanyRole(self, role):

        self.driver.find_element(By.XPATH,self.txtcustomerrole_xpath).click()

        time.sleep(2)

        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstadmrole_xpath)

        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH,self.lstfmoderator_xpath)

        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH,self.lstregister_xpath)

        elif role == "Guests":
            #self.driver.find_element(By.XPATH,self.rmvcrs_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstguest_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH,self.lstvendor_xpath)

        self.driver.execute_script("arguments[0].click();",self.listitem)


    def setMangerVendor(self,value):
        drp = self.driver.find_element(By.XPATH,self.txtmanvendors_xpath)
        drp.select_by_visible_text(value)

    def activeRd(self):
        self.driver.find_element(By.ID,self.rdactive_id).click()

    def changePassword(self):
        self.driver.find_element(By.ID,self.rdchangepswd_id).click()

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtcustcomment_xpath).send_keys(content)

    def cLickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath).click()


