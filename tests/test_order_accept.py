import allure
import pytest
import json
from helpers.helpers_order import ScooterApiOrder
from helpers.helpers_courier import ScooterApiCourier
from data import ResponseText


@allure.feature('Проверка ручки "Принять заказ"')
class TestOrderAccept:
    @allure.title('Проверка успешного запроса на принятие заказа')
    def test_order_success_accept(self, create_courier_random):
        courier = create_courier_random
        courier_id = ScooterApiCourier.login_courier(courier[0], courier[1]).json()['id']
        order_track = ScooterApiOrder.create_order().json()['track']
        order_id = ScooterApiOrder.get_order_track(order_track).json()['order']['id']
        response = ScooterApiOrder.accept_order(courier_id, order_id)
        assert response.status_code == 200 and response.text == ResponseText.text_tru

    @allure.title('Проверка запроса на принятие заказа без id курьера')
    def test_order_success_accept(self, create_courier_random):
        courier = create_courier_random
        order_track = ScooterApiOrder.create_order().json()['track']
        order_id = ScooterApiOrder.get_order_track(order_track).json()['order']['id']
        response = ScooterApiOrder.accept_order('', order_id)
        response_text = response.json()["message"]
        assert response.status_code == 400 and response_text == ResponseText.text_courier_order_accept_insufficient_data


    @allure.title('Проверка запроса на принятие заказа без id заказа')
    def test_order_success_accept(self, create_courier_random):
        courier = create_courier_random
        courier_id = ScooterApiCourier.login_courier(courier[0], courier[1]).json()['id']
        order_track = ScooterApiOrder.create_order().json()['track']
        response = ScooterApiOrder.accept_order(courier_id, '')
        response_text = response.json()["message"]
        assert response.status_code == 400 and response_text == ResponseText.text_courier_order_accept_insufficient_data

    @allure.title('Проверка запроса на принятие заказа c некорректным id курьера')
    def test_order_success_accept(self, create_courier_random):
        courier = create_courier_random
        courier_id = ScooterApiCourier.login_courier(courier[0], courier[1]).json()['id']
        order_track = ScooterApiOrder.create_order().json()['track']
        order_id = ScooterApiOrder.get_order_track(order_track).json()['order']['id']
        response = ScooterApiOrder.accept_order((courier_id+1), order_id)
        response_text = response.json()["message"]
        assert response.status_code == 404 and response_text == ResponseText.text_courier_order_accept_incorrect_courier

    @allure.title('Проверка запроса на принятие заказа c некорректным id заказа')
    def test_order_success_accept(self, create_courier_random):
        courier = create_courier_random
        courier_id = ScooterApiCourier.login_courier(courier[0], courier[1]).json()['id']
        order_track = ScooterApiOrder.create_order().json()['track']
        order_id = ScooterApiOrder.get_order_track(order_track).json()['order']['id']
        response = ScooterApiOrder.accept_order(courier_id, (order_id+1))
        response_text = response.json()["message"]
        assert response.status_code == 404 and response_text == ResponseText.text_courier_order_accept_incorrect_order