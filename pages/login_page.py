from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginLocators:
    url = "https://test-hg.isi-technology.com/"
    username_locator = "[placeholder='Username']"
    password_locator = "[placeholder='Password']"
    checkbox_locator = "accept_terms_and_conditions"
    submit_locator = "//button[contains(@class, 'login-button') and contains(text(), 'Log in')]"

class Login(BasePage):

    def login_func(self, username, password):
        input_name = self.find_element((By.CSS_SELECTOR, LoginLocators.username_locator))
        input_name.send_keys(username)
        input_password = self.find_element((By.CSS_SELECTOR, LoginLocators.password_locator))
        input_password.send_keys(password)
        checkbox = self.find_element((By.NAME, LoginLocators.checkbox_locator))
        if not checkbox.is_selected():
            checkbox.click()
        submit_button = self.find_element((By.XPATH, LoginLocators.submit_locator))
        submit_button.click()

