import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import Keys


class InputOrderHelper(BasePage):
    data_pick_field = (By.XPATH, ".//input[contains(@placeholder, 'Когда привезти самокат')]")
    rental_period_field = (By.XPATH, ".//div[contains(@aria-haspopup, 'listbox')]")
    comment_field = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий для курьера')]")
    scooter_color_black_checkbox = (By.XPATH, ".//input[@id='black']")
    scooter_color_grey_checkbox =  (By.XPATH, ".//input[@id='grey']")
    next_page_button = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)")
    yes_button = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)")
    order_info_modal_window = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']")

    def set_date(self, date_needed):
        self.driver.find_element(*self.data_pick_field).click()
        self.driver.find_element(*self.data_pick_field).send_keys(date_needed)
        self.driver.find_element(*self.data_pick_field).send_keys(Keys.ENTER)

    def set_rental_period(self, rental_period):
        self.driver.find_element(*self.rental_period_field).click()
        self.driver.find_element(By.XPATH, f'.//div[contains(text(), "{rental_period}")]').click()

    def set_scooter_color(self, checkbox):
        self.driver.find_element(*checkbox).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).click()
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def click_next_page_button(self):
        self.driver.find_element(*self.next_page_button).click()

    @allure.step('Кликнуть по кнопке завершения оформления "Заказать')
    def click_to_create_order_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Заполнить информацию о заказе')
    def input_data(self, date_needed, rental_period, checkbox, comment):
        self.set_date(date_needed)
        self.set_rental_period(rental_period)
        self.set_scooter_color(checkbox)
        self.set_comment(comment)
        self.click_next_page_button()
