import time

from .base_page import BasePage
from selenium.webdriver.common.by import By

class AlertLocators:

    logo_locator = (By.XPATH, "//img[contains(@class, 'brand-logo-img') and @ng-src='images/HG_logo.png']")
    alert_button_locator = (By.XPATH, "//span[text()='Alerts']")
    add_alert_locator = (By.XPATH, "//div[@class='flex']/div")
    placeholder_name_locator = (By.CSS_SELECTOR, "[placeholder='Name']")
    placeholder_temperature_from_locator = (By.CSS_SELECTOR, "[placeholder='Temperature From']")
    placeholder_temperature_to_locator = (By.CSS_SELECTOR, "[placeholder='Temperature To']")
    placeholder_search_location_locator = (By.CSS_SELECTOR, "[placeholder='Search Location']")
    office_row_locator = (By.XPATH, "//td[@title='Office' and contains(@class, 'no-wrap')]")
    button_save_locator = (By.XPATH, "//button[contains(text(), 'Save')]")
    message_proof_locator = (By.XPATH, "//div[@class='message ng-binding' and contains(text(), 'Test-1 was created.')]")
    message_invalid_locator = (By.XPATH, "//div[@class='message ng-binding' and contains(text(), 'This field may not be blank.')]")

class AlertPage(BasePage):

    def alert_valid(self):
        logo_element = self.wait_for_element(AlertLocators.logo_locator)
        assert logo_element.is_displayed()
        alert_button = self.find_element(AlertLocators.alert_button_locator)
        alert_button.click()
        add_alert_element = self.wait_for_element(AlertLocators.add_alert_locator)
        add_alert_element.click()
        placeholder_name = self.wait_for_element(AlertLocators.placeholder_name_locator)
        placeholder_name.send_keys('Test-1')
        placeholder_temperature_from = self.find_element(AlertLocators.placeholder_temperature_from_locator)
        placeholder_temperature_from.send_keys('2')
        placeholder_temperature_to = self.find_element(AlertLocators.placeholder_temperature_to_locator)
        placeholder_temperature_to.send_keys('10')
        placeholder_search_location = self.find_element(AlertLocators.placeholder_search_location_locator)
        placeholder_search_location.send_keys('Office')
        office_row = self.wait_for_element(AlertLocators.office_row_locator)
        office_row.click()
        button_save = self.find_element(AlertLocators.button_save_locator)
        button_save.click()
        button_save.click()
        message_proof = self.wait_for_element(AlertLocators.message_proof_locator)
        assert message_proof.text == 'Test-1 was created.'
        time.sleep(5)

    def alert_invalid(self):
        logo_element = self.wait_for_element(AlertLocators.logo_locator)
        assert logo_element.is_displayed()
        alert_button = self.find_element(AlertLocators.alert_button_locator)
        alert_button.click()
        add_alert_element = self.wait_for_element(AlertLocators.add_alert_locator)
        add_alert_element.click()
        placeholder_temperature_from = self.find_element(AlertLocators.placeholder_temperature_from_locator)
        placeholder_temperature_from.send_keys('2')
        placeholder_temperature_to = self.find_element(AlertLocators.placeholder_temperature_to_locator)
        placeholder_temperature_to.send_keys('10')
        placeholder_search_location = self.find_element(AlertLocators.placeholder_search_location_locator)
        placeholder_search_location.send_keys('Office')
        office_row = self.wait_for_element(AlertLocators.office_row_locator)
        office_row.click()
        button_save = self.find_element(AlertLocators.button_save_locator)
        button_save.click()
        button_save.click()
        message_invalid = self.wait_for_element(AlertLocators.message_invalid_locator)
        assert message_invalid.text == 'This field may not be blank.'








