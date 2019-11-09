from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementNotVisibleException
from polling import TimeoutException, poll
import logging
from selenium.webdriver.common.keys import Keys
from os.path import dirname, join
import Driver

LOGGER = logging.getLogger(__name__)

def getElementByXPath(selector):
    """
    Get the element from XPath
    :param selector:
    :return boolean:
    """
    try:
        element = Driver.Instance.find_element_by_xpath(selector)
        # highlight(element)
        return element

    except NoSuchElementException:
        return False

def getUrl(url):
    """
    Hits the URL
    :param url:
    :return:
    """
    Driver.Instance.get(url)

def isElementPresentByXPath(selector):
    """
    Checks if the element is Present
    :param selector:
    :return boolean:
    """
    try:
        if getElementByXPath(selector):
            return True
    except NoSuchElementException:
        return False

def clickByXPath(selector):
    """
    Clicks on a element
    :param selector:
    :return boolean:
    """

    try:
        button = getElementByXPath(selector)
        # highlight(button)
        button.click()
        return True
    except ElementNotInteractableException:
        return False
    except StaleElementReferenceException:
        return False
    except NoSuchElementException:
        return False
    except Exception:
        raise Exception("COULD NOT CLICK THE ELEMENT")

def enterTextByXPath(selector, text):
    """
    Enters text into the text field
    :param selector:
    :param text:
    :return boolean:
    """

    try:
        text_field = getElementByXPath(selector)
        # highlight(text_field)

        text_field.clear()
        text_field.send_keys(text)
        return True
    except ElementNotInteractableException:
        return False

def sendBackspace(selector, numOfBackspace = 1):
    """
    Send number of backspaces to the field
    :param selector:
    :return:
    """
    try:
        text_field = getElementByXPath(selector)
    except ElementNotInteractableException:
        return False
    text_field.click()
    for i in range(numOfBackspace):
        text_field.send_keys(Keys.BACKSPACE)

def closeTab():
    """
    closes a tab
    :return: None
    """
    Driver.Instance.execute_script("window.close()")

def waitForPageLoad():
    """
    Waits till the web page returns 'complete' status for document.readyState
    :return: page_state
    """

    try:
        page_state = Driver.Instance.execute_script('return document.readyState;')
        poll(lambda: page_state == 'complete', timeout=20, step=1)
        return page_state
    except TimeoutException:
        return TimeoutError

def selectCheckbox(selector, name, deselect=False):
    """
    Selects the checkbox with a given name
    :param selector:
    :param name:
    :param deselect:
    :return:
    """

    found_checkbox = False
    checkboxes = getElementByXPath(selector)
    for checkbox in checkboxes:
        if checkbox.get_attribute('name') == name:
            found_checkbox = True
            if not deselect and not checkbox.is_selected():
                checkbox.click()
            if deselect and checkbox.is_selected():
                checkbox.click()

    if not found_checkbox:
        raise Exception('Checkbox %s not found.' % name)

def returnText(selector):
    """
    Returns Text on passing a selector
    :param selector:
    :return: Text
    """
    try:
        element = getElementByXPath(selector)
        # highlight(element)
        return element.text
    except NoSuchElementException:
        raise Exception("Never saw {0}".format(selector))

def highlight(element):
    """
    Highlights a Selenium WebDriver element
    :param element:
    :return higlighted web-element:
    """

    waitForPageLoad()
    parent_ele = element.find_element_by_xpath('..')
    highlighted = Driver.Instance.execute_script("arguments[0].setAttribute('style', arguments[1]);", parent_ele,
                                                 "color: black; border: 4px solid red;")
    return highlighted

def verifyTitle(title):
    """
    Verifies the title of the WebPage
    :param title:
    :return boolean:
    """
    try:
        poll(lambda: Driver.Instance.title == title, timeout = 6, step = 1)
        return True
    except NoSuchElementException:
        return False
    except Exception:
        LOGGER.debug("Page title mismatch")
        return False
    finally:
        LOGGER.info("\nExpected title : {0}\n Actual Title : {1}\n".format(title, Driver.Instance.title))

def getListOfElements(selector):
    """
    Returns list of Web-elements on passing a selector
    :param selector:
    :return: List of Web-elements
    """
    try:
        listOfElements = Driver.Instance.find_elements_by_xpath(selector)
        return listOfElements
    except NoSuchElementException:
        raise Exception('Never saw %s' % selector)

def clickByElement(element):
    """
    Clicks by web element
    :param element:
    :return: boolean
    """
    try:
        element.click()
        return True
    except ElementNotInteractableException:
        return False
    except StaleElementReferenceException:
        return False
    except NoSuchElementException:
        return False

def resetImplicitWait(seconds):
    """
    Resets Implicit wait which is set during Driver Initialization
    :param seconds:
    :return:
    """
    Driver.Instance.implicitly_wait(seconds)

def isElementDisplayedByXPath(selector):
    """
    Checks if the element is Displayed
    :param selector:
    :return boolean:
    """

    try:
        getElementByXPath(selector).is_displayed()
        return True
    except ElementNotVisibleException:
        return False

def takeScreenShot(name = "sampleShot.png"):
    """
    This function will take screenshots and save them in the folder name screenshots
    :param name: (str) name of the screenshots with extension
    :return: None
    """
    project_root = dirname(dirname(__file__))
    output_path = join(project_root, 'airbnb-selenium/screenshots/{0}'.format(name))
    Driver.Instance.save_screenshot(output_path)
