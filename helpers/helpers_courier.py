import requests
import random
import string
import allure
from data import ApiUrl
class ScooterApiCourier:

    @staticmethod
    @allure.step('Регистрация курьера с рандомными данными')
    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(ApiUrl.API_URL_CREATE_COURIER, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass


    @staticmethod
    @allure.step('Регистрация курьера с постоянными данными')
    def registration_courier_stable(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(ApiUrl.API_URL_CREATE_COURIER, data=payload)
        return response

    @staticmethod
    @allure.step('Вход в систему')
    def login_courier(login: str, password: str):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(ApiUrl.API_URL_LOGIN, data=payload)
        return response

    @staticmethod
    @allure.step('Получить ID курьера')
    def get_courier_id(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(ApiUrl.API_URL_LOGIN, data=payload)
        return response.json()['id']

    @staticmethod
    @allure.step('Удалить курьера в системе')
    def delete_courier(id_courier):
        response = requests.delete(f'{ApiUrl.API_URL_CREATE_COURIER}/{id_courier}')
        return response




