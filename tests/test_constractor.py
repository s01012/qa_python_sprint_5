from selenium.webdriver.common.by import By
import locators


def test_transition_to_sauce_click_on_button_added_new_class_to_div(driver_setup, generator):
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_constractor_sauce).click()
    element_sauce_value = driver.find_element(By.XPATH, locators.link_constractor_sauce)
    assert 'tab_tab_type_current__2BEPc' in element_sauce_value.get_attribute("class")
    driver.quit()

def test_transition_to_filling_click_on_button_added_new_class_to_div(driver_setup, generator):
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_constractor_filling).click()
    element_sauce_value = driver.find_element(By.XPATH, locators.link_constractor_filling)
    assert 'tab_tab_type_current__2BEPc' in element_sauce_value.get_attribute("class")
    driver.quit()

def test_transition_to_bun_click_on_button_added_new_class_to_div(driver_setup, generator):
    driver = driver_setup
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, locators.link_constractor_filling).click()
    driver.find_element(By.XPATH, locators.link_constractor_bun).click()
    element_sauce_value = driver.find_element(By.XPATH, locators.link_constractor_bun)
    assert 'tab_tab_type_current__2BEPc' in element_sauce_value.get_attribute("class")
    driver.quit()
