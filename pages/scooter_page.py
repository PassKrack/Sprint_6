import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ScooterPageLocators:
    QUESTION1_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Сколько это стоит? И как оплатить?')]")
    ANSWER1_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    QUESTION2_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Хочу сразу несколько самокатов! Так можно?')]")
    ANSWER2_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    QUESTION3_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Как рассчитывается время аренды?')]")
    ANSWER3_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    QUESTION4_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]")
    ANSWER4_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    QUESTION5_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Можно ли продлить заказ или вернуть самокат раньше?')]")
    ANSWER5_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    QUESTION6_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Вы привозите зарядку вместе с самокатом?')]")
    ANSWER6_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    QUESTION7_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Можно ли отменить заказ?')]")
    ANSWER7_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    QUESTION8_LOCATOR = (By.XPATH, ".//div[contains(text(), 'Я жизу за МКАДом, привезёте?')]")
    ANSWER8_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-7']/p")
    ORDER_BUTTON1_LOCATOR = (By.XPATH, ".//div[2]/button[contains(text(), 'Заказать')]")
    ORDER_BUTTON2_LOCATOR = (By.XPATH, ".//button[contains(@class, 'Button_UltraBig__UU3Lp')]")
    YANDEX_LOGO_LOCATOR = (By.XPATH, ".//img[@src='/assets/ya.svg']")
    SCOOTER_LOGO_LOCATOR = (By.XPATH, ".//img[@src='/assets/scooter.svg']")
    HOME_HEADER_LOCATOR = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")


class ScooterPageHelper(BasePage):

    @allure.step('Кликнуть по вопросу')
    def click_on_the_question(self, question_locator):
        self.find_element(question_locator, time=5).click()

    @allure.step('Сохранить ответ')
    def check_answer(self, answer_locator):
        answer_text = self.find_element(answer_locator, time=5).text
        return answer_text
