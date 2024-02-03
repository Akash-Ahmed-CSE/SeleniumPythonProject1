from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By

class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["Name"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getCheckBox().click()
        self.selectOptionBytext(homepage.getGender(),getData["Gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param