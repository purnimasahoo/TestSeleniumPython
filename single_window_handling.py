#Step 1: Here, we import the important Selenium Python libraries that will enable us to perform our test.
#These include pytest, WebDriver, By, BrowserOptions, WebDriverWait, and expected_conditions.

#We import pytest, as it is Selenium Python’s primary unit testing tool.
# The imported Selenium WebDriver is a web framework that automates cross browser tests.
#The By query is used to locate specific web elements using the find_element() method.
# The explicit wait time implements the WebDriverWait class combined with the expected_conditions class to define the wait
# for a certain condition to be executed before proceeding to the next part of the code.
# Lastly, the Options class customizes the specified browser driver sessions. For this instance, we are using the ChromeOptions
# classes.
import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

def test_single_window_chrome():

    # We generate options using the LambdaTest Automation Capabilities Generator according to the browser we use to run the
    # automated tests. We create an instance of the Options class, set the conditions, and pass it to the driver constructor.
    options = ChromeOptions()
    options.browser_version = '103.0'
    options.platform_name = 'Windows 10'
    lt_options = {}
    lt_options['username'] = os.environ.get('LT_USERNAME')
    lt_options['accesskey'] = os.environ.get('LT_ACCESS_KEY')
    lt_options['project'] = 'SingleWindowHandling'
    lt_options['selenium_version'] = '4.1.2'
    lt_options['w3c'] = True
    options.set_capability('LT:options', lt_options)
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    #We set the username and accesskey provided in the LambdaTest Profile page to a remote_url variable that connects us to
    # the Remote Selenium Grid (@hub.lambdatest.com/wd/hub). We then use the remote_url and options to instantiate the
    # corresponding web browser (Chrome).
    remote_url = "https://" + user_name + ":" + \
                 accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    driver.get('https://www.lambdatest.com/selenium-playground')
    driver.maximize_window()
    # Look for the window popup modal link and click
    #We open the LambdaTest Playground website, then maximize the browser window to locate the web element with the link to
    # the Window Popup Demo Page.Right-click the “Windows Popup Modal” link and click inspect to open the browser inspect tool.
    # The web element is located using its href tag.We use the driver. current_window_handle method to obtain the parent window’s
    # unique id and store it as a string.
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href="https://www.lambdatest.com/selenium-playground/window-popup-modal-demo"]')))
    element.click()
    # Get the window handle Id of the current parent window
    parent_guid = driver.current_window_handle
    print(f"The parent window guid is: {parent_guid}")
    #We then locate the web element with the button “Follow on Twitter” using its title and click on it to open a
    # child window.
    twitter_element = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Follow @Lambdatesting on Twitter"]')))
    twitter_element.click()
    # Get the window handle ids of all the windows opened
    #We store the window handles of the opened windows in a variable called all_guid.
    all_guid = driver.window_handles
    # iterate through the guids and if there is a parent window id skip it and switch to the new window
    #We then switch to the child window using the driver.switch_to.window(guid) method.
    # The code iterates through the stored window handles, and if it comes across the parent window handle,
    # it skips over it and switches to the child window. Then the child window’s ID is printed.
    # The driver.close() method closes the currently active child window and will quit the driver session if the child
    # window is the only active window.
    for guid in all_guid:
        if guid != parent_guid:
            driver.switch_to.window(guid)
            print(f"The child guid is: {guid}")
            driver.close()

    driver.quit()