from pages import Homepage, ExperiencePage, SearchResultPage
import time, logging
from autologging import traced, logged
import unittest
import Driver
import pytest
from utils import commonFunctionsUI, pyUtils

LOGGER = logging.getLogger(__name__)

@pytest.mark.mobile
@pytest.mark.web
class BookingTest(unittest.TestCase):
    """
    A happy path booking test which will select
    - select destination at home page
    - guests in search result page
    - price filter in experience page
    This script is quite unstable as the elements on airbnb keeps changing every time
    """
    def setUp(self):
        Driver.initialize()
        self.homePage = Homepage.homepage()
        self.experiencePage = ExperiencePage.experiencePage()
        self.SearchPage = SearchResultPage.searchResultPage()

        # Go to the set url
        self.homePage.goToURL()

    @traced
    @logged
    def test_sample_booking(self):
        self.homePage.checkBookingFormLoad()
        time.sleep(3)
        try:
            self.homePage.waitAndAcceptCookies()
        except:
            pass

        # enter destination and select dates and search
        self.homePage.enterDestination(destination = "Sicily, Italy")
        self.homePage.clickOnFirstSearchResult()
        self.homePage.selectDateFromTable()
        time.sleep(2)

        self.homePage.selectDateFromTable(offsetInDays = 90)
        self.homePage.clickOnSearch()
        commonFunctionsUI.waitForPageLoad()

        # select guests on search result page
        time.sleep(3)
        assert commonFunctionsUI.verifyTitle(title = "Sicily · Airbnb")
        self.SearchPage.selectGuests()
        commonFunctionsUI.waitForPageLoad()
        self.homePage.clickOnExperiences()

        commonFunctionsUI.waitForPageLoad()
        assert commonFunctionsUI.verifyTitle(title = "Things to Do in Sicily | 5-Star Authentic Experiences")

        # select price on experience page
        try:
            self.experiencePage.filterPrice()
        except:
            LOGGER.error("Could not filter price")

            # Select first and third experience
            self.SearchPage.selectFirstAndThirdPlaceToStay()

    def tearDown(self):
        time.sleep(2)
        Driver.quitDriver()
