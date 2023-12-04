import time

from pages.locators import SbisContacsPageLocators as SbCoPaLo
from pages.locators import Urls
from pages.sbis_pages import SbisContactsPage, SbisDownloadPage, SbisMainPage
from pages.tensor_pages import TensorAboutPage, TensorMainPage


def test_first_case(driver):
    page = SbisMainPage(driver, Urls.SBIS_MAIN_URL)
    page.open()
    page.click_on_contacts_menu_item()
    contacts_page = SbisContactsPage(driver, driver.current_url)
    contacts_page.click_on_tensor_banner()
    contacts_page.switch_to_new_tab()
    tensor_main_page = TensorMainPage(driver, driver.current_url)
    tensor_main_page.close_cookie_agreement_notification()
    tensor_main_page.should_be_sila_v_lyudyah_block()
    tensor_main_page.click_on_podrobnee_in_sila_v_lyudyah_block()
    tensor_about_page = TensorAboutPage(driver, driver.current_url)
    tensor_about_page.should_be_tensor_about_url()
    tensor_about_page.should_be_same_sized_images_in_rabotaem_block()


def test_second_case(driver):
    page = SbisMainPage(driver, Urls.SBIS_MAIN_URL)
    page.open()
    page.click_on_contacts_menu_item()
    contacts_page = SbisContactsPage(driver, driver.current_url)
    contacts_page.should_be_expected_region(SbCoPaLo.MOSCOW_REGION_INFO)
    partners_list = contacts_page.get_partners_list()
    contacts_page.change_region(SbCoPaLo.KAMCHATKA_SELECTOR)
    contacts_page.should_be_expected_region(SbCoPaLo.KAMCHATKA_REGION_INFO)
    contacts_page.should_be_partners_list_change(partners_list)


def test_third_case(driver):
    page = SbisMainPage(driver, Urls.SBIS_MAIN_URL)
    page.open()
    page.close_cookie_agreement_notification()
    page.click_on_download_sbis_link()
    download_page = SbisDownloadPage(driver, driver.current_url)
    time.sleep(1)
    download_page.click_on_sbis_plugin_menu_item()
    download_page.click_on_download_web_installer()
    download_page.check_file_size()

