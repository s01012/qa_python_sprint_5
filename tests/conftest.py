import pytest
import random
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture
def default_user():
    dict_authorization = {'email': 'kesha_qa_11@gmail.com',
                          'password': 'qwe123'}
    return dict_authorization

@pytest.fixture
def generator():
    alphabet = [chr(i) for i in range(97, 123)]

    dict_registration = {
        'name': 'Иннокентий(aka Эльдар)',
        'email': (''.join(random.sample(alphabet, 4)) + f'_qa_{random.randint(100, 999)}@gmail.com'),
        'password': random.randint(100000, 999999)
    }
    return dict_registration

