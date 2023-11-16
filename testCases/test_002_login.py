import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import os


class TestLogin():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("**** starting test login ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage = self.lp.textisExistornot()
        if self.targetpage == True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshorts\\" + "test_login")
            self.driver.close()
            assert False


        self.logger.info("*** end the test_002_login*****")
