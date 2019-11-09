from pages import Homepage, ExperiencePage, SearchResultPage
import time
import unittest
import Driver
import pytest
import logging
from utils import commonFunctionsUI
from autologging import traced,logged

LOGGER = logging.getLogger(__name__)

@traced
@logged
@pytest.mark.mobile
@pytest.mark.web
class BookingTest(unittest.TestCase):
    """
    A happy path booking test which will select destination, date, and guests at home page
    and will apply price at search result page and then click on first and third experience
    """
    def setUp(self):
        Driver.initialize()
        self.homePage = Homepage.homepage()
        self.experiencePage = ExperiencePage.experiencePage()
        self.SearchPage = SearchResultPage.searchResultPage()

        # Go to the set url
        self.homePage.goToURL()


    def test_sample_booking(self):
        self.homePage.checkBookingFormLoad()
        time.sleep(3)
        try:
            self.homePage.waitAndAcceptCookies()
        except:
            pass

        # enter destination and select filters
        self.homePage.enterDestination(destination = "Sicily, Italy")
        self.homePage.clickOnFirstSearchResult()
        self.homePage.selectDateFromTable(offsetInDays = 10)
        time.sleep(2)
        self.homePage.selectDateFromTable(offsetInDays = 100)
        self.homePage.selectGuests()
        # commonFunctionsUI.takeScreenShot(name = "homePage.png")
        self.homePage.clickOnSearch()

        # wait for search to work and verify the title
        commonFunctionsUI.waitForPageLoad()
        time.sleep(3)
        assert commonFunctionsUI.verifyTitle(title = "Sicily · Stays · Airbnb")

        # Price button is very unstable/sporadic
        try:
            self.SearchPage.filterPrice()
        except:
            LOGGER.error("Could not select Price")

        # Select first and third experience
        self.SearchPage.selectFirstAndThirdPlaceToStay()

    def tearDown(self):
        time.sleep(2)
        Driver.quitDriver()
