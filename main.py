# Implementation of Selenium test automation for this Selenium Python Tutorial
# Step 1 – The necessary modules are imported, namely pytest, sys, selenium, time, etc
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


# Step 2 – The test name starts with test_ (i.e. test_todo_app) so that pytest is able to identify the test.
# Using the Selenium WebDriver command, the Chrome WebDriver is instantiated. The URL is passed using the .get method
# in Selenium.

def test_todo_app():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()

    # Step 3 – The Inspect Tool feature of the Chrome browser is used to get the details of the required web elements
    # i.e. checkboxes with name li1 & li2 and button element with id = addbutton.
    # Once the web elements are located using the appropriate Selenium methods
    # [i.e. find_element_by_name(), find_element_by_id()], necessary operations [i.e. click(), etc.] are performed
    # on those elements.
    chrome_driver.find_element("name", "li1").click()
    chrome_driver.find_element("name", "li2").click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element("id", "sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)

    chrome_driver.find_element("id", "addbutton").click()
    sleep(5)

    output_str = chrome_driver.find_element("name", "li6").text
    sys.stderr.write(output_str)

    # Step 4 – The close() method of Selenium is used to release the resources held by the WebDriver instance.
    sleep(2)
    chrome_driver.close()
