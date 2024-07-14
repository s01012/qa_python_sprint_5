import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators

def test_constractor_click_on_link_constractor_identical_curent_url_value(default_user):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_account_button).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_account_button).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_constractor).click()
    time.sleep(5)
    _value = driver.find_element(By.XPATH, locators.personal_input_login)

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()
