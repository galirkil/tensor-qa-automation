import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def driver():
    print('\nstart browser for test..')
    options = Options()
    options.add_experimental_option(
        'prefs', {'download.default_directory': BASE_DIR}
    )
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nquit browser..')
    driver.quit()
