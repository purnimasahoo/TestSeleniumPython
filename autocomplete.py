#Step 1:Import the Selenium WebDriver and WebDriver Manager modules that are needed for
# Selenium WebDriver to use ChromeDriver to interact with the browser.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def test_todo_app():

    #step 2: you have to instantiate the driver in a variable called “browser”.
    # We are instantiating the ChromeDriver, given that we will use it in the Chrome browser
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
    browser.maximize_window()

    #We should create a first_name variable to store this element. We use the browser instance to call the
    # find_element method. The method’s first parameter is the way that the element will be located,
    # in this case, using the ID. So, we use the By function followed by the value ID.
    first_name = browser.find_element(By.ID, "input-firstname")

    #Then, after locating the element, we need to interact with it.
    # In this First Name field, we need to fill in with the user’s first name, so our action will be
    # typing inside the field.
    first_name.send_keys("FirstName")
    last_name = browser.find_element(By.ID, "input-lastname")
    telephone = browser.find_element(By.ID, "input-telephone")
    email = browser.find_element(By.ID, "input-email")

    last_name.send_keys("LastName")
    email.send_keys("your-email@example.com")
    telephone.send_keys("+351999888777")

    password = browser.find_element(By.ID, "input-password")
    password_confirm = browser.find_element(By.ID, "input-confirm")
    password.send_keys("123456")
    password_confirm.send_keys("123456")

    #To locate the newsletter Yes option, we will also use the find_element method of Selenium WebDriver.
    # The first parameter of this method will be By.XPATH, which says that we are now using the XPath to
    # locate the element

    newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")

    #To click in the Yes option, we should use the action “click” in the element.
    newsletter.click()

    continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
    continue_button.click()

    assert browser.title == "Register Account"
    sleep(20)
    browser.quit()
