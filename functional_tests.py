# Import the `webdriver` module from the Selenium library
from selenium import webdriver

# Create a new instance of the Firefox WebDriver
browser = webdriver.Chrome()

# Instruct the browser to navigate to the URL 'http://localhost:8000',
# which is a local server hosting a web application.
browser.get('http://localhost:8000')

# Check whether the string 'Django' is present in the title of the current web page.
assert(browser.title)