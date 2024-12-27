from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "pass")
        self.login_button = (By.ID, "send2")
        self.wrong_password_error = (By.XPATH, "//div[@role='alert']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def error_message_visible(self):
        try:
            error = self.driver.find_element(*self.wrong_password_error)
            return error.is_displayed()  # This will return True if the error message is visible
        except:
            return False  # Return False if the error element is not found
