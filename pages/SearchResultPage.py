import time

from utils import commonFunctionsUI
from configs.prod import urls
import Driver

class locators:
    def __init__(self):
        """
        constructor to set the locators
        """
        self.guests = "//*[contains(text(), \"Guests\")]"
        self.twoGuests = "//*[contains(text(), \"2 guests\")]"

        self.increaseValue ="//button[contains(@aria-label, \"increase value\")]"
        self.altIncreaseValueAdult = "//div[@class='_1rev4gc']//div//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]"
        self.altIncreaseValueChild = "//div[@class='_10ejfg4u']//div[2]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]"
        self.guestsListSave = "//button[text()='Save']"
        self.guestsListSave2 = "//div[@class='_1rev4gc']//div//button[@class='_b0ybw8s'][contains(text(),'Save')]"
        self.exploreSiciliyDiv = "//div[contains(text(),'Explore Sicily')]"

        self.priceButton = "//button[@id='menuItemButton-price_range']"
        self.maxPrice = "//*[@id='price_filter_max']"
        self.minPrice = "//*[@id='price_filter_min']"
        self.priceButton2 = "//*[@id='menuItemButton-price_range']/button"
        self.applyPrice = "//button[contains(text(),'Apply')]"
        self.placesToStayContainer = "//div[@itemprop='itemListElement']"

class searchResultPage:
    def __init__(self):
        self.locators = locators()

    def selectGuests(self):
        """
        Select one adult and a child
        :return: None
        """
        # click on guests button
        lst = commonFunctionsUI.getListOfElements(selector = self.locators.guests)
        commonFunctionsUI.clickByElement(lst[0])

        commonFunctionsUI.resetImplicitWait(3)

        # select adult and child
        try:
            lst = commonFunctionsUI.getListOfElements(selector = self.locators.increaseValue)
            try:
                commonFunctionsUI.clickByElement(lst[0])
            except:
                pass
            try:
                commonFunctionsUI.clickByElement(lst[1])
            except:
                pass
        except:
            commonFunctionsUI.clickByXPath(selector = self.locators.altIncreaseValueAdult)
            commonFunctionsUI.clickByXPath(selector = self.locators.altIncreaseValueChild)

        # click on save button
        try:
            lst = commonFunctionsUI.getListOfElements(selector = self.locators.guestsListSave)
            try:
                commonFunctionsUI.clickByElement(lst[0])
                commonFunctionsUI.clickByElement(lst[1])
            except:
                pass

        except:
            commonFunctionsUI.clickByXPath(selector = self.locators.guestsListSave2)
        commonFunctionsUI.resetImplicitWait(10)

    def filterPrice(self, price = 5000):
        """
        Set the minimum price to 5000 and click apply
        :param price: (int) minimum price
        :return: None
        """
        try:
            commonFunctionsUI.clickByXPath(selector = self.locators.priceButton)
        except:
            commonFunctionsUI.clickByXPath(selector = self.locators.priceButton2)

        if commonFunctionsUI.isElementDisplayedByXPath(selector = self.locators.priceButton):
            commonFunctionsUI.clickByXPath(selector = self.locators.minPrice)
            commonFunctionsUI.sendBackspace(selector = self.locators.minPrice, numOfBackspace = 7)
            commonFunctionsUI.enterTextByXPath(selector = self.locators.minPrice, text = price)
        else:
            raise Exception("Price button not found")
        commonFunctionsUI.clickByXPath(selector = self.locators.applyPrice)

    def selectFirstAndThirdPlaceToStay(self):
        """
        Select first and third places according to the filters
        :return: None
        """
        if commonFunctionsUI.isElementDisplayedByXPath(selector = self.locators.placesToStayContainer):
            lst = commonFunctionsUI.getListOfElements(selector = self.locators.placesToStayContainer)
            commonFunctionsUI.clickByElement(element = lst[0])
            commonFunctionsUI.waitForPageLoad()
            commonFunctionsUI.closeTab()
            commonFunctionsUI.clickByElement(element = lst[2])

