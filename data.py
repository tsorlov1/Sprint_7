courier_data = ['ninja030624', '1234', 'saske']
order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

class ApiUrl:
    API_URL = 'https://qa-scooter.praktikum-services.ru/'
    API_URL_LOGIN = f'{API_URL}api/v1/courier/login'
    API_URL_CREATE_COURIER = f'{API_URL}api/v1/courier'
    API_URL_CREATE_ORDER = f'{API_URL}api/v1/orders'
    API_URL_GET_ORDER_TRACK = f'{API_URL}api/v1/orders/track'
    API_URL_ORDER_ACCEPT = f'{API_URL}api/v1/orders/accept/'

class ResponseText:
    text_tru = '{"ok":true}'
    text_courier_delete_insufficient_data = 'Недостаточно данных для удаления курьера'
    text_courier_delete_not_found = 'Курьера с таким id нет'
    text_courier_login_insufficient_data = 'Недостаточно данных для входа'
    text_courier_login_incorrect_data = 'Учетная запись не найдена'
    text_courier_registration_double_login = 'Этот логин уже используется'
    text_courier_registration_insufficient_data = 'Недостаточно данных для создания учетной записи'
    text_courier_order_accept_insufficient_data = 'Недостаточно данных для поиска'
    text_courier_order_accept_incorrect_courier = 'Курьера с таким id не существует'
    text_courier_order_accept_incorrect_order = 'Заказа с таким id не существует'
    text_courier_order_get_incorrect_track = 'Заказ не найден'

