import time
import logging
from utils import commonFunctionsUI
from autologging import traced,logged

LOGGER = logging.getLogger(__name__)

@traced
@logged
class locators:
    def __init__(self):
        self.price = "//*[contains(text(), \"Price\")]"

        self.minPrice = "self.minPrice ='//*[@id='price_filter_min']'"
        self.priceSave = "//button[@id='filter-panel-save-button']"
        self.placesToStayContainer = "//div[@itemprop='itemListElement']"
        self.searchButton = "/html/body/div[5]/div/div[2]/header/div/div/div[2]/div/div/div/div/form/div[4]/div/button"
@traced
@logged
class experiencePage:
    def __init__(self):
        self.locators = locators()

    def filterPrice(self, minPrice = 5000):
        """
        Set the minimum price to 500
        :param maxPrice: (int) minimum price
        :return: None
        """

        # Check and select if price button is displayed
        if commonFunctionsUI.isElementDisplayedByXPath(selector = self.locators.price):
            commonFunctionsUI.clickByXPath(selector = self.locators.price)
        else:
            LOGGER.error("Could not click price button")
            raise Exception("could not click price button")

        time.sleep(3)


        try:
            commonFunctionsUI.clickByXPath(selector = self.locators.minPrice)
            commonFunctionsUI.sendBackspace(selector = self.locators.priceSave, numOfBackspace = 5)

            commonFunctionsUI.enterTextByXPath(selector = self.locators.minPrice, text = minPrice)
        except:
            try:
                commonFunctionsUI.clickByXPath(selector = self.locators.searchButton)
            except:
                commonFunctionsUI.clickByXPath(selector = self.locators.priceSave)
            LOGGER.error("Could not find input field to enter min price")
            raise Exception("Could not find input field to enter min price")


        if commonFunctionsUI.isElementDisplayedByXPath(selector = self.locators.priceSave):
            commonFunctionsUI.clickByXPath(selector = self.locators.priceSave)
        else:
            raise Exception("Could not click on save price button")

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