import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators


def test_registration_click_on_registration_button_identical_email_value(generator):

    driver = webdriver.Chrome()
    driver.maximize_window()


    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(By.XPATH, locators.link_account_button).click()
    driver.find_element(By.XPATH, locators.link_sign_up).click()
    driver.find_element(By.XPATH, locators.name_input_registration_form).send_keys(generator.get('name'))
    driver.find_element(By.XPATH, locators.email_input_registration_form).send_keys(generator.get('email'))
    driver.find_element(By.XPATH, locators.password_input_registration_form).send_keys(generator.get('password'))
    driver.find_element(By.XPATH, locators.registration_button_registration_form).click()

    WebDriverWait(driver, 15).until(expected_conditions.
                                   visibility_of_element_located((By.XPATH, locators.email_input_authorization_form)))

    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(generator.get('email'))

    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(generator.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.link_account_button)))

    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.
                                     visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == generator.get('email')

    driver.quit()

def test_registration_click_on_registration_button_error_message(generator):

    driver = webdriver.Chrome()
    driver.maximize_window()


    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(By.XPATH, locators.link_account_button).click()
    driver.find_element(By.XPATH, locators.link_sign_up).click()
    driver.find_element(By.XPATH, locators.name_input_registration_form).send_keys(generator.get('name'))
    time.sleep(3)
    driver.find_element(By.XPATH, locators.email_input_registration_form).send_keys(generator.get('email'))
    time.sleep(3)
    driver.find_element(By.XPATH, locators.password_input_registration_form).send_keys(str(generator.get('password'))[:-1])
    time.sleep(3)

    driver.find_element(By.XPATH, locators.registration_button_registration_form).click()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, locators.incorrect_password_message)
    assert error_message.text == 'Некорректный пароль'
    driver.quit()