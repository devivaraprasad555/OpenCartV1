from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    txt_email = "//input[@id='input-email']"
    txt_password = "//input[@id='input-password']"
    btn_login = "button[type='submit']"
    text_wraping = "form[id='form-login'] h2"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login).click()

    def textisExistornot(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.text_wraping).is_displayed()
        except:
            return False
