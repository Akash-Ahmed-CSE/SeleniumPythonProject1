import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()

        # Navigate to "Shop"
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopIteam()
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  #From HomePage Class
        log.info("getting all the card titles")
        #checkOutPage = CheckOutPage(self.driver)
        cards = checkOutPage.getCardTitles()
        #cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                #self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getPrimaryButton().click()
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        time.sleep(2)
        checkOutPage.checkOutItems().click()
        #self.driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-success']").click()
        log.info("Entering the Country Name as Ind")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
        time.sleep(2)

        self.verifyLinkPresence("India")
        # wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        success = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Text received from the Application is "+success)
        assert "Success! Thank you!" in success

        # driver.get_screenshot_as_file("screen.png")
        time.sleep(3)