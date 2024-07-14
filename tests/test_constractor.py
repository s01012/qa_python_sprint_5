import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators


def test_transition_to_sauce_click_on_button_added_new_class_to_div(generator):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_constractor_sauce).click()
    time.sleep(5)
    element_sauce_value = driver.find_element(By.XPATH, locators.link_constractor_sauce)
    print(element_sauce_value.get_attribute("class"))
    assert 'tab_tab_type_current__2BEPc' in element_sauce_value.get_attribute("class")
    driver.quit()

def test_transition_to_filling_click_on_button_added_new_class_to_div(generator):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_constractor_filling).click()
    time.sleep(5)
    element_sauce_value = driver.find_element(By.XPATH, locators.link_constractor_filling)
    assert 'tab_tab_type_current__2BEPc' in element_sauce_value.get_attribute("class")
    driver.quit()

def test_transition_to_bun_click_on_button_added_new_class_to_div(generator):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_constractor_filling).click()
    time.sleep(5)
    driver.find_element(By.XPATH, locators.link_constractor_bun).click()
    time.sleep(5)
    element_sauce_value = driver.find_element(By.XPATH, locators.link_constractor_bun)
    assert 'tab_tab_type_current__2BEPc' in element_sauce_value.get_attribute("class")
    driver.quit()