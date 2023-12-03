from selenium.webdriver.common.by import By


class Urls:
    SBIS_MAIN_URL = 'https://sbis.ru/'
    TENSOR_ABOUT_URL = 'https://tensor.ru/about'


class SbisMainPageLocators:
    CONTACTS_MENU_ITEM = (By.CSS_SELECTOR, '.sbisru-Header__menu-item-1 a')
    DOWNLOAD_SBIS_LINK = (By.XPATH, '//a[text()="Скачать СБИС"]')
    CLOSE_COOKIE_AGREEMENT_NOTIFICATION = (
        By.CSS_SELECTOR,
        '.sbis_ru-CookieAgreement__close'
    )


class SbisContacsPageLocators:
    TENSOR_BANNER = (By.CSS_SELECTOR, '#contacts_clients a[title="tensor.ru"]')
    CHANGE_REGION_BUTTON = (
        By.CSS_SELECTOR,
        '.sbisru-Contacts__relative .sbis_ru-Region-Chooser__text'
    )
    KAMCHATKA_SELECTOR = (
        By.CSS_SELECTOR,
        '[title="Камчатский край"]'
    )
    TATARSTAN_REGION_INFO = {
        'name': 'Республика Татарстан',
        'slug': '16-respublika-tatarstan',
    }
    KAMCHATKA_REGION_INFO = {
        'name': 'Камчатский край',
        'slug': '41-kamchatskij-kraj',
    }
    PARTNERS_LIST = (
        By.CSS_SELECTOR,
        '[data-qa="items-container"]'
    )


class SbisDownloadPageLocators:
    SBIS_PLUGIN_MENU_ITEM = (
        By.CSS_SELECTOR,
        '[data-id="plugin"] .controls-tabButton__overlay'
    )
    DOWNLOAD_WEB_INSTALLER_LINK = (
        By.XPATH,
        '//a[contains(text(), "Exe")]'
    )


class TensorMainPageLocators:
    CLOSE_COOKIE_AGREEMENT_NOTIFICATION = (
        By.CLASS_NAME,
        'tensor_ru-CookieAgreement__close'
    )
    SILA_V_LYUDYAH_BLOCK = (
        By.XPATH,
        '//div[@class="tensor_ru-Index__block4-content tensor_ru-Index__card"]'
        '/p[text()="Сила в людях"]'
    )
    SILA_V_LYUDYAH_BLOCK_PODROBNEE_ = (
        By.CSS_SELECTOR, '.tensor_ru-Index__block4-content a'
    )


class TensorAboutPageLocators:
    RABOTAEM_BLOCK_IMAGES = (By.CLASS_NAME, 'tensor_ru-About__block3-image')
