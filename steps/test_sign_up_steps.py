from behave import given, when, then
from pages.sign_up_page import SignUpPage


@given('the user navigates to the sign-up page')
def test_step_impl(context):
    # Initialize the driver and navigate to the sign-up page
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    context.driver.maximize_window()
    context.sign_up_page = SignUpPage(context.driver)


@when(
    'the user enters registration details with first name "{first_name}", last name "{last_name}", email "{email}", '
    'password "{password}", and confirm password "{confirm_password}"')
def test_step_impl(context, first_name, last_name, email, password, confirm_password):
    # Enter the values from the feature file into the sign-up form
    context.sign_up_page.enter_first_name(first_name)
    context.sign_up_page.enter_last_name(last_name)
    context.sign_up_page.enter_email(email)
    context.sign_up_page.enter_password(password)
    context.sign_up_page.enter_confirm_password(confirm_password)
    context.sign_up_page.click_sign_up()


@then('the user should be registered successfully')
def test_step_impl(context):
    # Verify that the registration was successful, e.g., by checking the page title
    assert "My Account" in context.driver.title
    context.driver.quit()
