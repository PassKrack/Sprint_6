import allure
import pytest

from default_data import questions_data
from pages.scooter_page import ScooterPageHelper, ScooterPageLocators


class TestScootersImportantQuestions:

    @pytest.mark.parametrize("user_data", questions_data)
    @allure.title('При клике на первый вопрос открывается корректный ответ')
    def test_success_correct_answer_for_question1(self, browser, user_data):
        scooter_main_page = ScooterPageHelper(browser)
        scooter_main_page.go_to_site()
        scooter_main_page.scroll_page(user_data["question"])
        scooter_main_page.click_on_the_question(user_data["question"])
        answer = scooter_main_page.check_answer(user_data["answer_text"])
        assert answer == user_data["answer"]

