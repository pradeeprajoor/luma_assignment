from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    # Use the Service object to specify the path to the ChromeDriver
    service = Service(ChromeDriverManager().install())  # Automatically download and install the latest ChromeDriver
    context.driver = webdriver.Chrome(service=service)


def after_all(context):
    context.driver.quit()
