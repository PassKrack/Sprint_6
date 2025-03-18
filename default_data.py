from pages.about_order_page import InputOrderHelper
from pages.scooter_page import ScooterPageLocators

DZEN_URL = "https://dzen.ru/?yredirect=true"

user_info = [
    {
        "order_button": ScooterPageLocators.ORDER_BUTTON1_LOCATOR,
        "name": 'Игорь',
        "surname": 'Фомин',
        "address":'Чистые пруды 8',
        "metro_station":'Чистые пруды',
        "phone_number":'89876543210',
        "date_needed":'21.03.2025',
        "rental_period":'сутки',
        "checkbox":InputOrderHelper.SCOOTER_COLOR_BLACK_CHECKBOX,
        "comment":'В первой половине дня'
    },
    {
        "order_button": ScooterPageLocators.ORDER_BUTTON2_LOCATOR,
        "name": 'Виктор',
        "surname": 'Петров',
        "address": 'Красногвардейская 13',
        "metro_station":'Красногвардейская',
        "phone_number":'89871234567',
        "date_needed":'23.03.2025',
        "rental_period":'двое суток',
        "checkbox":InputOrderHelper.SCOOTER_COLOR_GREY_CHECKBOX,
        "comment":'Во второй половине дня'
    }
]

questions_data = [
    {
        "question": ScooterPageLocators.QUESTION1_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER1_LOCATOR,
        "answer": 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'},
    {
        "question": ScooterPageLocators.QUESTION2_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER2_LOCATOR,
        "answer": 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'},
    {
        "question": ScooterPageLocators.QUESTION3_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER3_LOCATOR,
        "answer": 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'},
    {
        "question": ScooterPageLocators.QUESTION4_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER4_LOCATOR,
        "answer": 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'},
    {
        "question": ScooterPageLocators.QUESTION5_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER5_LOCATOR,
        "answer": 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'},
    {
        "question": ScooterPageLocators.QUESTION6_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER6_LOCATOR,
        "answer": 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'},
    {
        "question": ScooterPageLocators.QUESTION7_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER7_LOCATOR,
        "answer": 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'},
    {
        "question": ScooterPageLocators.QUESTION8_LOCATOR,
        "answer_text": ScooterPageLocators.ANSWER8_LOCATOR,
        "answer": 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'}
]