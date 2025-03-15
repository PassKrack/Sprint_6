import allure

from pages.scooter_page import ScooterPageLocators, ScooterPageHelper


class TestRouting:

    @allure.title('При нажатии на логотип "Яндекс" происходит редирект на страницу Дзен')
    @allure.description('Нажимаем на логотип Яндекс и проверяем, что открывается новая вкладка браузера с Яндекс Дзен')
    def test_success_routing_by_yandex_logo(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.click_to_order_button(ScooterPageLocators.YANDEX_LOGO_LOCATOR)
        new_url = scooter_main_page.load_new_window()
        assert new_url == "https://dzen.ru/?yredirect=true"

    @allure.title('При нажатии на логотип ""Самокат" происходит переход на главную страницу')
    @allure.description('Нажимаем на лого Самоката и проверяем, что открывается главная страница сайта')
    def test_success_routing_by_scooter_logo(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.check_element_is_enabled(ScooterPageLocators.ORDER_BUTTON1_LOCATOR)
        scooter_main_page.click_to_order_button(ScooterPageLocators.ORDER_BUTTON1_LOCATOR)
        scooter_main_page.click_to_order_button(ScooterPageLocators.SCOOTER_LOGO_LOCATOR)
        assert ScooterPageLocators.HOME_HEADER_LOCATOR