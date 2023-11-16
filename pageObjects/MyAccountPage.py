from selenium.webdriver.common.by import By


class MyAccountPage:

    lnk_logout_xpath = "//aside[@id='colum-right']//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_elements(By.XPATH,self.lnk_logout_xpath).click()



