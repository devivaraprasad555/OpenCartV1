import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        # home page
        self.logger.info("***test_001_AccountRegistration started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Lauching application ")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("clicking on Registration ")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        # account registration page
        self.logger.info("Providing the registration details ")
        self.repage = AccountRegistrationPage(self.driver)
        self.repage.setFirstName("prasad")
        self.repage.setLastName("vinay")
        self.email = randomString.random_string_generator()
        self.repage.setEmail(self.email)
        self.repage.setPassword("vinay12345")
        self.repage.checkBox()
        self.repage.AgreeBox()
        self.repage.clickButton()
        # self.items = self.repage.items_elemnts()
        # if self.items == "desktops":
        #     self.logger.info("sucessfully items is showing  ")
        #     assert True
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshorts\\"+"test_account_reg.png")
        #     self.logger.error("sucessfully items is not showing ")
        #     self.driver.close()
        self.driver.close()
        self.logger.info("***test_001_AccountRegistration finished ***")


