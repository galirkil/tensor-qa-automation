from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import (TensorAboutPageLocators, TensorMainPageLocators,
                            Urls)


class TensorMainPage(BasePage):
    def close_cookie_agreement_notification(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                TensorMainPageLocators.CLOSE_COOKIE_AGREEMENT_NOTIFICATION
            )
        ).click()

    def should_be_sila_v_lyudyah_block(self):
        assert self.is_element_present(
            *TensorMainPageLocators.SILA_V_LYUDYAH_BLOCK
        ), 'Блок "Сила в людях" не найден!'

    def click_on_podrobnee_in_sila_v_lyudyah_block(self):
        self.driver.find_element(
            *TensorMainPageLocators.SILA_V_LYUDYAH_BLOCK_PODROBNEE_
        ).click()


class TensorAboutPage(BasePage):
    def should_be_tensor_about_url(self):
        url = self.driver.current_url
        assert url == Urls.TENSOR_ABOUT_URL, (
            f'Wrong url! Expected {Urls.TENSOR_ABOUT_URL}, got {url} instead'
        )

    def should_be_same_sized_images_in_rabotaem_block(self):
        images = self.driver.find_elements(
            *TensorAboutPageLocators.RABOTAEM_BLOCK_IMAGES
        )
        image_sizes = [image.size for image in images]

        for image_size in image_sizes:
            assert image_size['height'] == image_sizes[0]['height'], (
                'Высота изображений в блоке "Работаем" неодинакова'
            )
            assert image_size['width'] == image_sizes[0]['width'], (
                'Ширина изображений в блоеке "Работаем" неодинакова'
            )
