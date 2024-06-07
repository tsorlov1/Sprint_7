import allure
import pytest
from helpers.helpers_courier import ScooterApiCourier


@allure.feature('проверка ручки удаления курьера')
class TestCourierDelete:
    @allure.title('Проверка успешного удаления курьера')
    def test_courier_success_delete(self):
        login_pass = ScooterApiCourier.register_new_courier_and_return_login_password()
        courier_id = ScooterApiCourier.get_courier_id(login_pass[0], login_pass[1])
        response = ScooterApiCourier.delete_courier(courier_id)
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверка удаления курьера без указания id в запросе')
    def test_courier_delete_without_id(self):
        response = ScooterApiCourier.delete_courier('')
        response_text = response.json()["message"]
        assert response.status_code == 400 and response_text == 'Недостаточно данных для удаления курьера'

    @allure.title('Проверка удаления курьера c указанием несуществующего id в запросе')
    def test_courier_delete_incorrect_id(self):
        response = ScooterApiCourier.delete_courier('50')
        response_text = response.json()["message"]
        assert response.status_code == 404 and response_text == 'Курьера с таким id нет'
