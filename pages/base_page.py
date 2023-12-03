from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def switch_to_new_tab(self):
        """
        Switch focus to new opened tab or window.
        Works only for two opened tabs/windows.
        """
        current_tab = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))

        for tab in self.driver.window_handles:
            if tab != current_tab:
                self.driver.switch_to.window(tab)
                break

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
