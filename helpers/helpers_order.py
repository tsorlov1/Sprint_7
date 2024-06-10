import requests
import allure
import json
from data import ApiUrl, order_data


class ScooterApiOrder:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order():
        order_data_string = json.dumps(order_data)
        response = requests.post(ApiUrl.API_URL_CREATE_ORDER, data=order_data_string)
        return response

    @staticmethod
    @allure.step('Получить заказ по его номеру')
    def get_order_track(track_order):
        payload = {
            "t": track_order
        }
        response = requests.get(ApiUrl.API_URL_GET_ORDER_TRACK, params=payload)
        return response

    @staticmethod
    @allure.step('Принять заказ')
    def accept_order(courier_id, order_id):
        payload = {
            "courierId": courier_id
        }
        response = requests.put(f'{ApiUrl.API_URL_ORDER_ACCEPT}{order_id}', params=payload)
        return response


    @staticmethod
    @allure.step('Получение списка заказов по id курьера')
    def get_list_order(courier_id):
        payload = {
            "courierId": courier_id
        }
        response = requests.get(ApiUrl.API_URL_CREATE_ORDER, params=payload)
        return response
