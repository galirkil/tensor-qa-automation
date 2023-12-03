from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import SbisContacsPageLocators, SbisMainPageLocators


class SbisMainPage(BasePage):
    def click_on_contacts_menu_item(self):
        self.driver.find_element(
            *SbisMainPageLocators.CONTACTS_MENU_ITEM
        ).click()

    def close_cookie_agreement_notification(self):
        self.driver.find_element(
            *SbisMainPageLocators.CLOSE_COOKIE_AGREEMENT_NOTIFICATION
        ).click()

class SbisContactsPage(BasePage):
    def click_on_tenzor_banner(self):
        self.driver.find_element(
            *SbisContacsPageLocators.TENZOR_BANNER
        ).click()

    def change_region(self, region_locator: tuple):
        self.driver.find_element(
            *SbisContacsPageLocators.CHANGE_REGION_BUTTON
        ).click()
        self.driver.find_element(
            *region_locator
        ).click()

    def should_be_expected_slug_in_url(self, slug: str):
        WebDriverWait(self.driver, 7).until(
            ec.url_changes(self.driver.current_url)
        )
        url = self.driver.current_url
        assert slug in url, (
            f'Wrong url!'
            f'Expected {slug!r} in {url!r}'
        )

    def should_be_expected_title(self, expected_string: str):
        title = self.driver.title
        assert expected_string in title, (
            f'Wrong title!'
            f'Expected {expected_string!r} in {title!r}'
        )

    def should_be_expected_region_name(self, expected_name: str):
        name = self.driver.find_element(
            *SbisContacsPageLocators.CHANGE_REGION_BUTTON
        ).text
        assert name == expected_name, (
            f'Wrong region name!'
            f'Expected {expected_name!r}, got {name!r}'
        )
