import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        self.dzen_url = "https://dzen.ru/?yredirect=true"

    @allure.step('Открыть страницу "https://qa-scooter.praktikum-services.ru/"')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    @allure.step('Загрузить новую вкладку браузера')
    def load_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(ec.url_to_be(self.dzen_url))
        url = self.driver.current_url
        return url

    def scroll_page(self, locator):
        element = self.find_element(locator, time=7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    @allure.step('Кликнуть на кнопку "Заказать" на главной странице')
    def click_to_order_button(self, order_button):
        self.find_element(order_button).click()

    def check_element_is_enabled(self, order_button):
        return self.find_element(order_button).is_enabled()

