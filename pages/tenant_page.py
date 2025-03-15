import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TenantPageLocators:

    TENANT_HEADER_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Для кого самокат')]")

class InputTenantHelper(BasePage):

    name_field = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    surname_field = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    address_field = (By.XPATH, ".//input[contains(@placeholder, 'Адрес: куда привезти заказ')]")
    metro_station_field = (By.XPATH, ".//input[contains(@placeholder, 'Станция метро')]")
    phone_number_field = (By.XPATH, ".//input[contains(@placeholder, 'Телефон: на него позвонит курьер')]")
    next_page_button = (By.XPATH, ".//button[contains(text(),'Далее')]")

    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_field).click()
        self.driver.find_element(By.XPATH, f'.//div[text()="{metro_station}"]').click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    @allure.step('Кликнуть по кнопке "Далее"')
    def click_next_page_button(self):
        self.driver.find_element(*self.next_page_button).click()

    @allure.step('Заполнить информацию об арендаторе')
    def input_data(self, name, surname, address, metro_station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        self.click_next_page_button()