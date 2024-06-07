import allure
import pytest
from helpers.helpers_courier import ScooterApiCourier


@allure.feature('Проверка ручки "Авторизация курьера"')
class TestCourierLogin:
    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_success_login(self, create_courier_random):
        courier = create_courier_random
        login = courier[0]
        password = courier[1]
        response = ScooterApiCourier.login_courier(login, password)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка авторизации курьера при заполнении не всех обязательных полей')
    @pytest.mark.parametrize('login_courier, password_courier',
                             [
                                 ('ninja030624', ''),
                                 ('', '1234')
                             ])
    def test_courier_login_required_field(self, create_courier_stable, login_courier, password_courier):
        courier = create_courier_stable
        ScooterApiCourier.registration_courier_stable(courier[0], courier[1], courier[2])
        response = ScooterApiCourier.login_courier(login_courier, password_courier)
        response_text = response.json()["message"]
        assert response.status_code == 400 and response_text == 'Недостаточно данных для входа'

    @allure.title('Проверка авторизации курьера при введении логина или пароля с ошибкой')
    @pytest.mark.parametrize('login_courier, password_courier',
                             [
                                 ('ninja030625', '1234'),
                                 ('ninja030624', '1235')
                             ])
    def test_courier_login_incorrect_login_or_password(self, create_courier_stable, login_courier, password_courier):
        courier = create_courier_stable
        ScooterApiCourier.registration_courier_stable(courier[0], courier[1], courier[2])
        response = ScooterApiCourier.login_courier(login_courier, password_courier)
        response_text = response.json()["message"]
        assert response.status_code == 404 and response_text == 'Учетная запись не найдена'
