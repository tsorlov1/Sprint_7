import allure
import pytest
from helpers.helpers_courier import ScooterApiCourier
from data import ResponseText


@allure.feature('Проверка ручки регистрация курьера')
class TestCourierRegistration:
    @allure.title('Проверка успешной регистрации курьера')
    def test_courier_success_registration(self, create_courier_stable):
        courier = create_courier_stable
        response = ScooterApiCourier.registration_courier_stable(courier[0], courier[1], courier[2])
        assert response.status_code == 201 and response.text == ResponseText.text_tru

    @allure.title('Проверка ошибки при создания курьера с уже существующим логином')
    def test_courier_registration_double_login(self, create_courier_random):
        courier = create_courier_random
        courier_login = courier[0]
        courier_pass = courier[1]
        courier_name = courier[2]
        response = ScooterApiCourier.registration_courier_stable(courier_login, courier_pass, courier_name)
        response_text = response.json()['message']
        assert response.status_code == 409 and response_text == ResponseText.text_courier_registration_double_login

    @allure.title('Проверка ввода обязательных полей при регистрации курьера')
    @pytest.mark.parametrize('login, password',
        [
            ('login',''),
            ('', 'password')
        ])
    def test_courier_registration_required_field(self, login, password):
        response = ScooterApiCourier.registration_courier_stable(login, password, 'name')
        response_text = response.json()['message']
        assert response.status_code == 400 and response_text == ResponseText.text_courier_registration_insufficient_data
