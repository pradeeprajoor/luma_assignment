from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "firstname")
        self.last_name = (By.ID, "lastname")
        self.email = (By.ID, "email_address")
        self.password = (By.ID, "password")
        self.confirm_password = (By.ID, "password-confirmation")
        self.sign_up_button = (By.XPATH, "//button[@title='Create an Account']")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(*self.confirm_password).send_keys(password)

    def click_sign_up(self):
        self.driver.find_element(*self.sign_up_button).click()
