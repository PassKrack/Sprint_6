import allure
import pytest

from default_data import user_info
from pages.about_order_page import InputOrderHelper
from pages.scooter_page import ScooterPageHelper
from pages.tenant_page import InputTenantHelper


class TestMakeAnOrder:

    @pytest.mark.parametrize("user_data", user_info)
    @allure.title('Успешное создание заказа с заполением всех полей')
    @allure.description('Проверяем по-очередно обе кнопки "Заказать", что при заполнении всех полей заказ создается')
    def test_success_make_an_order_by_header_button(self, browser, user_data):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(user_data["order_button"])
        scooter_main_page.check_element_is_enabled(user_data["order_button"])
        scooter_main_page.click_to_order_button(user_data["order_button"])
        tenant_page = InputTenantHelper(browser)
        tenant_page.input_data(user_data["name"], user_data["surname"], user_data["address"], user_data["metro_station"], user_data["phone_number"])
        order_page = InputOrderHelper(browser)
        order_page.input_data(user_data["date_needed"], user_data["rental_period"], user_data["checkbox"], user_data["comment"])
        order_page.click_to_create_order_button()
        assert InputOrderHelper.order_info_modal_window

