from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage


@given('the user navigates to login page')
def test_step_impl(context):
    # Initialize the driver and navigate to the login page
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)


@when('the user enters invalid password with email "{email}" and password "{password}"')
def test_step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    context.login_page.click_login()


@then('the user should get valid error message')
def test_step_impl(context):
    # Add assertions to verify the login, such as checking if the user is redirected to the dashboard
    assert context.login_page.error_message_visible()
    context.driver.quit()
