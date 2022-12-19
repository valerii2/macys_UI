import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from abstract.selenium_listener import MyListener


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')    # use 'headless' if you don't need a browser UI / 'chrome' if UI need
    options.add_argument('--start-maximized')    # Starts the browser maximized, regardless of any previous settings
    options.add_argument('--window-size=1920,1080')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)   # executable_path='C:/Windows/chromedriver.exe' - if do you need set path
    return driver


@pytest.fixture(scope='function')    # function - each 'setup' test will start like clear browser ; session - each test will start in one common session
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, MyListener())  # use Listener and rewrite 'driver'
    url = 'https://www.macys.com/'  # website url for testing
    if request.cls is not None:           # checking - are there test classes in 'request'
        request.cls.driver = driver
    driver.get(url)              # if there are not classes in 'request' 'driver' get our url
    driver.delete_all_cookies()   # deleting all cookies for pass security checking on automation
    yield driver
    # driver.close() # close only the current tab in the browser
    driver.quit()   # close all browser


