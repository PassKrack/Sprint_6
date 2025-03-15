import allure

from pages.scooter_page import ScooterPageHelper, ScooterPageLocators


class TestScootersImportantQuestions:

    @allure.title('При клике на первый вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question1(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION1_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION1_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER1_LOCATOR)
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('При клике на второй вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question2(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION2_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION2_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER2_LOCATOR)
        assert answer == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('При клике на третий вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question3(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION3_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION3_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER3_LOCATOR)
        assert answer == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('При клике на четвертый вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question4(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION4_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION4_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER4_LOCATOR)
        assert answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('При клике на пятый вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question5(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION5_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION5_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER5_LOCATOR)
        assert answer == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('При клике на шестой вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question6(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION6_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION6_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER6_LOCATOR)
        assert answer == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('При клике на седьмой вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question7(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION7_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION7_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER7_LOCATOR)
        assert answer == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('При клике на восьмой вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question8(self, browser):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(ScooterPageLocators.QUESTION8_LOCATOR)
        scooter_main_page.click_on_the_question(ScooterPageLocators.QUESTION8_LOCATOR)
        answer = scooter_main_page.check_answer(ScooterPageLocators.ANSWER8_LOCATOR)
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'