from pages.about_order_page import InputOrderHelper
from pages.scooter_page import ScooterPageLocators

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
        "checkbox":InputOrderHelper.scooter_color_black_checkbox,
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
        "checkbox":InputOrderHelper.scooter_color_grey_checkbox,
        "comment":'Во второй половине дня'
    }
]