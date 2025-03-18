import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import Keys


class InputOrderHelper(BasePage):
    DATA_PICK_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Когда привезти самокат')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, ".//div[contains(@aria-haspopup, 'listbox')]")
    COMMENT_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий для курьера')]")
    SCOOTER_COLOR_BLACK_CHECKBOX = (By.XPATH, ".//input[@id='black']")
    SCOOTER_COLOR_GREY_CHECKBOX =  (By.XPATH, ".//input[@id='grey']")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)")
    YES_BUTTON = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)")
    ORDER_INFO_MODAL_WINDOW = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']")

    @allure.step('Заполнить поле "Дата"')
    def set_date(self, date_needed):
        self.driver.find_element(*self.DATA_PICK_FIELD).click()
        self.driver.find_element(*self.DATA_PICK_FIELD).send_keys(date_needed)
        self.driver.find_element(*self.DATA_PICK_FIELD).send_keys(Keys.ENTER)

    @allure.step('Заполнить поле "Время аренды"')
    def set_rental_period(self, rental_period):
        self.driver.find_element(*self.RENTAL_PERIOD_FIELD).click()
        self.driver.find_element(By.XPATH, f'.//div[contains(text(), "{rental_period}")]').click()

    @allure.step('Выбрать цвет самоката ')
    def set_scooter_color(self, checkbox):
        self.driver.find_element(*checkbox).click()

    @allure.step('Заполнить поле "Комментарий курьеру"')
    def set_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).click()
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    @allure.step('Кликнуть кнопку завершения заказа "Заказать"')
    def click_next_page_button(self):
        self.driver.find_element(*self.NEXT_PAGE_BUTTON).click()

    @allure.step('Кликнуть по кнопке завершения оформления "Заказать')
    def click_to_create_order_button(self):
        self.driver.find_element(*self.YES_BUTTON).click()

    @allure.step('Заполнить информацию о заказе')
    def input_data(self, date_needed, rental_period, checkbox, comment):
        self.set_date(date_needed)
        self.set_rental_period(rental_period)
        self.set_scooter_color(checkbox)
        self.set_comment(comment)
        self.click_to_create_order_button()
