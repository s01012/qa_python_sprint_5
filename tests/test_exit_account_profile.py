from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_exit_account_profile_click_on_button_exit_identical_current_url_value(driver_setup, default_user):
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_enter).click()
    driver.find_element(By.XPATH, locators.email_input_authorization_form).send_keys(default_user.get('email'))
    driver.find_element(By.XPATH, locators.password_input_authorization_form).send_keys(default_user.get('password'))
    driver.find_element(By.XPATH, locators.authorization_button_authorization_form).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                       checkout_button)))
    driver.find_element(By.XPATH, locators.link_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                                       exit_button)))
    driver.find_element(By.XPATH, locators.exit_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.
                                                                              authorization_button_authorization_form)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()
