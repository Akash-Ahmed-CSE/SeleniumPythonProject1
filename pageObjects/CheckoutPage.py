from selenium.webdriver.common.by import By
class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    primaryButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.CSS_SELECTOR, "button[class = 'btn btn-success']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
        # driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)
        #driver.find_elements(By.CSS_SELECTOR, ".card-footer button")
    def getPrimaryButton(self):
        return self.driver.find_element(*CheckOutPage.primaryButton)
        #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)
        #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()