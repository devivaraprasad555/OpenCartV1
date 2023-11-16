from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountRegistrationPage:
    txt_firstname = "firstname"
    txt_lastname = "lastname"
    txt_email = "email"
    txt_password = "password"
    check_box = "newsletter"
    agree_check_box = "agree"
    click_submit_css = "button[type='submit']"
    text_checking = "//h1[normalize-space()='Register Account']"
    items = '//li[@class="nav-item dropdown"]'

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password).send_keys(pwd)

    def checkBox(self):
        self.driver.find_element(By.NAME, self.check_box).click()

    def AgreeBox(self):
        self.driver.find_element(By.NAME, self.agree_check_box).click()

    def clickButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_submit_css).click()

    def textChecking(self):
        try:
            self.driver.find_element(By.XPATH,self.text_checking).is_displayed()
        except:
            return False

    # def items_elemnts(self):
    #     items_each = self.driver.find_elements(By.XPATH, self.items)
    #     for each in items_each:
    #         return each.text
