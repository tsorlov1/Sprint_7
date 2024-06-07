import allure
import data
import pytest
import json
from helpers.helpers_order import ScooterApiOrder
from helpers.helpers_courier import ScooterApiCourier


@allure.feature('Проверка ручки "Создать заказ"')
class TestOrderCreate:
    @allure.title('Проверка тела ответа при создания заказа')
    def test_order_create_body_track(self):
        response = ScooterApiOrder.create_order()
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверка возможности указания цветов BLACK или GREY, или оба цвета, или без цвета')
    @pytest.mark.parametrize(
        'color',
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_order_create_choice_color(self, color):
        data.order_data['color'] = color
        response = ScooterApiOrder.create_order()
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверка получение списка заказов по id курьера')
    def test_order_get_list(self, create_courier_random):
        courier = create_courier_random
        courier_id = ScooterApiCourier.login_courier(courier[0], courier[1]).json()['id']
        order_track = ScooterApiOrder.create_order().json()['track']
        order_id = ScooterApiOrder.get_order_track(order_track).json()['order']['id']
        ScooterApiOrder.accept_order(courier_id, order_id)
        response = ScooterApiOrder.get_list_order(courier_id)
        assert (response.status_code == 200 and courier_id == response.json()['orders'][0]['courierId'] and
                order_track == response.json()['orders'][0]['track'])

