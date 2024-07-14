import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators


def test_authorization_click_on_link_enter_identical_email_value(default_user):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_enter).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))

    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()

def test_authorization_click_on_link_account_button_identical_email_value(default_user):

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
    WebDriverWait(driver, 20).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()

def test_authorization_click_on_enter_button_identical_email_value(default_user):

    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_account_button).click()
    driver.find_element(By.XPATH, locators.link_sign_up).click()

    driver.find_element(By.XPATH, locators.enter_button_registration_form).click()

    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))

    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.link_account_button)))

    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()

def test_authorization_click_on_restore_button_identical_email_value(default_user):

    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_enter).click()
    driver.find_element(By.XPATH, locators.restore_password_button).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.enter_button_restore_form).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    time.sleep(5)
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    time.sleep(5)
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    time.sleep(5)
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.link_account_button)))
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()