from pages.base_page import BasePage
from pages.locators import SbisMainPageLocators


class SbisMainPage(BasePage):
    def click_on_contacts_menu_item(self):
        self.driver.find_element(
            *SbisMainPageLocators.CONTACTS_MENU_ITEM
        ).click()

    def close_cookie_agreement_notification(self):
        self.driver.find_element(
            *SbisMainPageLocators.CLOSE_COOKIE_AGREEMENT_NOTIFICATION
        ).click()
