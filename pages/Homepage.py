import time
from datetime import date, timedelta
from utils import commonFunctionsUI, pyUtils
from configs.prod import urls
import calendar
from autologging import traced,logged

@traced
@logged
class locators:
    def __init__(self):
        self.destination_search_box = "//input[@id='Koan-magic-carpet-koan-search-bar__input']"
        self.search_button = "//button[@class='_1vs0x720']"
        self.booking_form = "//h1[@class='_14i3z6h']"
        self.firstDestinationOption = "//li[@id='Koan-magic-carpet-koan-search-bar__option-0']//div[@class='_121z06r2']"
        self.acceptCookiesButton = "//button[@class='optanon-allow-all accept-cookies-button']"
        self.experiencesLink = "//li[2]//div[1]//div[1]//a[1]//div[1]//div[1]//div[2]//div[1]//img[1]"
        self.dateXpath = "//td[contains(@aria-label, \"currentDate\")]"
        self.nextMonthArrow = "//div[@class='_1h5uiygl']"
        self.guests = "//*[contains(text(), \"Guests\")]"

        self.addAdult = "//div[@class='_9cfq872']//div//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]"
        self.addChild = "//div[@class='_e296pg']//div[2]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]"
        self.saveGuestList = "//button[@class='_b0ybw8s']"

class homepage:
    def __init__(self):
        self.locators = locators()

    def goToURL(self, URL = None):
        url = URL if URL else urls.base_url

        commonFunctionsUI.getUrl(url = url)
        commonFunctionsUI.waitForPageLoad()

    def checkBookingFormLoad(self):
        commonFunctionsUI.isElementPresentByXPath(selector = self.locators.booking_form)

    def enterDestination(self, destination):
        """
        This method will enter destination place on homepage
        :param destination: name of the place
        :return: None
        """
        commonFunctionsUI.enterTextByXPath(selector = self.locators.destination_search_box, text = destination)

    def clickOnFirstSearchResult(self):
        """
        It will click on the first result of destination
        :return: None
        """
        commonFunctionsUI.isElementPresentByXPath(selector = self.locators.firstDestinationOption)
        if not commonFunctionsUI.clickByXPath(selector = self.locators.firstDestinationOption):
            commonFunctionsUI.clickByXPath(selector = self.locators.firstDestinationOption)

    def clickOnSearch(self):
        """
        Click on the search button
        :return: None
        """
        commonFunctionsUI.isElementPresentByXPath(selector = self.locators.search_button)
        commonFunctionsUI.clickByXPath(selector = self.locators.search_button)

    def waitAndAcceptCookies(self):
        """
        Click ok in cookies popup
        :return: None
        """
        commonFunctionsUI.isElementPresentByXPath(selector = self.locators.acceptCookiesButton)
        commonFunctionsUI.clickByXPath(selector = self.locators.acceptCookiesButton)

    def clickOnBlankSpace(self):
        commonFunctionsUI.clickByXPath(selector = "//div[@class='_1n8ekdm']")

    def clickOnExperiences(self):
        """
        Click on experience tab
        :return: None
        """
        commonFunctionsUI.isElementPresentByXPath(selector = self.locators.experiencesLink)
        commonFunctionsUI.clickByXPath(selector = self.locators.experiencesLink)

    def selectDateFromTable(self, offsetInDays = 0):
        """
        Select date in date picker
        :param offsetInDays: days to add while selecting date
        :return: None
        """
        # get todays date and add number of days
        currentDate = date.today()
        requiredDate = currentDate+timedelta(days = offsetInDays)
        day = requiredDate.day
        year = requiredDate.year
        month = requiredDate.month
        monthInWords = calendar.month_name[month]

        # get the differnece in months based on days
        diff_months = pyUtils.diff_month(requiredDate, currentDate)
        for i in range(diff_months):
            commonFunctionsUI.clickByXPath(selector = self.locators.nextMonthArrow)
            time.sleep(2)

        # convert it to format which matches the xpath and then click
        currentDate = monthInWords+" "+str(day)+", "+str(year)
        commonFunctionsUI.clickByXPath(selector = self.locators.dateXpath.replace("currentDate",currentDate))

    def clickOnNextMonthArrow(self):
        """
        Click on next month arroe
        :return: None
        """
        commonFunctionsUI.isElementPresentByXPath(selector = self.locators.nextMonthArrow)
        commonFunctionsUI.isElementDisplayedByXPath(selector = self.locators.nextMonthArrow)
        commonFunctionsUI.clickByXPath(selector = self.locators.nextMonthArrow)

    def selectGuests(self):
        """
        Select different type of guests
        :return: None
        """
        lst = commonFunctionsUI.getListOfElements(selector = self.locators.guests)
        commonFunctionsUI.clickByElement(lst[0])

        commonFunctionsUI.resetImplicitWait(3)

        commonFunctionsUI.clickByXPath(selector = self.locators.addAdult)
        commonFunctionsUI.clickByXPath(selector = self.locators.addChild)
        commonFunctionsUI.clickByXPath(selector = self.locators.saveGuestList)
