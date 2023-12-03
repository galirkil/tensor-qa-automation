import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print('\nstart browser for test..')
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart browser for test..')
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print('\nquit browser..')
    driver.quit()
