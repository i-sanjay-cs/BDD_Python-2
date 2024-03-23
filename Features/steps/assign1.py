import os
from datetime import datetime
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define the directory to store screenshots
SCREENSHOT_DIR = "screenshots"

# Ensure the screenshots directory exists
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)


# Take a screenshot and save it with a timestamp as the filename
def take_screenshot(driver):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{now}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path


@given(u'User is on Home Page')
def step_user_on_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    take_screenshot(context.driver)


@when(u'User navigate to Login Page')
def step_user_navigate_to_login_page(context):
    context.driver.get('https://www.saucedemo.com/')
    take_screenshot(context.driver)


@then(u'User enters "{username}" and "{password}"')
def step_user_enters_credentials(context, username, password):
    username_field = context.driver.find_element(By.ID, "user-name")
    password_field = context.driver.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    take_screenshot(context.driver)


@then(u'Keeping case as "{case}"')
def step_keeping_case(context, case):
    print(f"Case: {case}")
    take_screenshot(context.driver)


@then(u'User should get logged in if "{case}" is Valid')
def step_user_should_get_logged_in(context, case):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()
    take_screenshot(context.driver)


@then(u'Message displayed Login Successfully if "{case}" is Valid')
def step_message_displayed_login_successfully(context, case):
    print("Login Successful")
    take_screenshot(context.driver)


@then(u'User will be asked to go back to login page if "{case}" is Invalid')
def step_user_asked_to_go_back_to_login_page(context, case):
    error_message = context.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    if error_message.is_displayed():
        print("Invalid credentials. Please go back to the login page.")
    take_screenshot(context.driver)


@then(u'Provide correct credentials if "{case}" is Invalid')
def step_provide_correct_credentials(context, case):
    # Provide correct credentials as per test scenario
    username_field = context.driver.find_element(By.ID, "user-name")
    password_field = context.driver.find_element(By.ID, "password")

    username_field.clear()
    username_field.send_keys("standard_user")
    password_field.clear()
    password_field.send_keys("secret_sauce")
    take_screenshot(context.driver)
