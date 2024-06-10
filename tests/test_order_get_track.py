import allure
import pytest
import json
from helpers.helpers_order import ScooterApiOrder
from data import ResponseText


@allure.feature('Проверка ручки "Принять заказ"')
class TestOrderGetTrack:
    def test_order_success_get(self):
        order_track = ScooterApiOrder.create_order().json()['track']
        response = ScooterApiOrder.get_order_track(order_track)
        assert response.status_code == 200 and 'order' in response.text

    def test_order_get_none_order_track(self):
        ScooterApiOrder.create_order().json()
        response = ScooterApiOrder.get_order_track('')
        response_text = response.json()["message"]
        assert response.status_code == 400 and response_text == ResponseText.text_courier_order_accept_insufficient_data

    def test_order_get_incorrect_order_track(self):
        order_track = ScooterApiOrder.create_order().json()['track']
        response = ScooterApiOrder.get_order_track(order_track+1)
        response_text = response.json()["message"]
        assert response.status_code == 404 and response_text == ResponseText.text_courier_order_get_incorrect_track