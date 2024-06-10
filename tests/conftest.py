import pytest
from helpers.helpers_courier import ScooterApiCourier
from data import courier_data



@pytest.fixture
def create_courier_stable():
    login_pass = courier_data
    yield login_pass

    courier_id = ScooterApiCourier.get_courier_id(login_pass[0], login_pass[1])
    ScooterApiCourier.delete_courier(courier_id)


@pytest.fixture
def create_courier_random():
    login_pass = ScooterApiCourier.register_new_courier_and_return_login_password()
    yield login_pass

    courier_id = ScooterApiCourier.get_courier_id(login_pass[0], login_pass[1])
    ScooterApiCourier.delete_courier(courier_id)


