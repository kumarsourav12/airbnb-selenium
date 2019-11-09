from selenium import webdriver
from os.path import dirname, join
from configs import variables
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import platform
import pyautogui
import logging
import sys
import autologging
from selenium.webdriver.support.ui import WebDriverWait

Instance = None
Waiter = None

def initialize():
    """Initializes the WebDriver based on the OS the test runs on"""

    global Instance, Waiter

    # Define a variable to hold all the configurations needed for Chrome Browser
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")

    # Get Root Path Of the Project
    project_root = dirname(dirname(__file__))
    output_path = join(project_root, 'airbnb-selenium/drivers')

    browser = variables.BROWSER

    chrome_driver_mac_path = os.path.join(output_path, 'chrome', 'chromedriver4')
    chrome_driver_windows_path = os.path.join(output_path, 'chrome', 'chromedriver.exe')
    gecko_driver_mac_path=os.path.join(output_path, 'firefox', 'geckodriver')
    gecko_driver_windows_path=os.path.join(output_path, 'firefox', 'geckodriver.exe')
    if browser == "Chrome":

        if platform.system() == "Darwin":

            # Create driver, pass it the path to the chrome driver file and the special configurations you want to run
            Instance = webdriver.Chrome(executable_path=chrome_driver_mac_path, options=chrome_options)

        elif platform.system() == "Windows":

            # Create driver, pass it the path to the chrome driver file and the special configurations you want to run
            Instance = webdriver.Chrome(executable_path=chrome_driver_windows_path, chrome_options=chrome_options)

    elif browser == "Firefox":

        caps = DesiredCapabilities().FIREFOX

        if platform.system() == "Darwin":

            # Create driver, pass it the path to the firefox driver file
            Instance = webdriver.Firefox(executable_path=gecko_driver_mac_path, capabilities=caps)

        elif platform.system() == "Windows":

            # Create driver, pass it the path to the firefox driver file
            Instance = webdriver.Firefox(executable_path=gecko_driver_windows_path, capabilities=caps)

    # # Set the browser window size
    width, height = pyautogui.size()
    Instance.set_window_size(width, height)

    # Initialize the Implicit Wait Time
    Instance.implicitly_wait(variables.IMPLICIT_WAIT_TIME)

    # Page Load Timeout
    Instance.set_page_load_timeout(variables.PAGE_LOAD_TIMEOUT)

    # Initializing WebDriver Wait, reset later wherever needed.
    Waiter = WebDriverWait(Instance, 10)
    Instance.delete_all_cookies()

def quitDriver():
    """Quits/Closes the WebDriver Instance on completing the test run"""

    global Instance

    Instance.quit()