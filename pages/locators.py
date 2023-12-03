from selenium.webdriver.common.by import By


class Urls:
    SBIS_MAIN_URL = 'https://sbis.ru/'
    TENZOR_ABOUT_URL = 'https://tensor.ru/about'


class SbisMainPageLocators:
    CONTACTS_MENU_ITEM = (By.CSS_SELECTOR, '.sbisru-Header__menu-item-1 a')
    DOWNLOAD_SBIS_LINK = (By.XPATH, '//a[text()="Скачать СБИС"]')
    CLOSE_COOKIE_AGREEMENT_NOTIFICATION = (
        By.CSS_SELECTOR,
        '.sbis_ru-CookieAgreement__close'
    )
