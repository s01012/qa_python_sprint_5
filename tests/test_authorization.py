from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_authorization_click_on_link_enter_identical_email_value(driver_setup, default_user):
    print("Запуск теста test_authorization_click_on_link_enter_identical_email_value")
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_enter).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                      email_input_authorization_form)))
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                    checkout_button)))
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                     visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    print("Тест test_authorization_click_on_link_enter_identical_email_value завершен успешно")
    driver.quit()

def test_authorization_click_on_link_account_button_identical_email_value(driver_setup, default_user):
    print("Запуск теста test_authorization_click_on_link_account_button_identical_email_value")
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                      email_input_authorization_form)))
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                       checkout_button)))
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()

def test_authorization_click_on_enter_button_identical_email_value(driver_setup, default_user):
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_account_button).click()
    driver.find_element(By.XPATH, locators.link_sign_up).click()
    driver.find_element(By.XPATH, locators.enter_button_registration_form).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                      email_input_authorization_form)))
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                       checkout_button)))
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()

def test_authorization_click_on_restore_button_identical_email_value(driver_setup, default_user):
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_enter).click()
    driver.find_element(By.XPATH, locators.restore_password_button).click()
    driver.find_element(By.XPATH, locators.enter_button_restore_form).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                      email_input_authorization_form)))
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                       checkout_button)))
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.
                                    visibility_of_element_located((By.XPATH, locators.personal_input_login)))
    email_value = driver.find_element(By.XPATH, locators.personal_input_login)
    assert email_value.get_attribute('value') == default_user.get('email')
    driver.quit()
