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


