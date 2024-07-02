from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

url = "https://www.saucedemo.com/"
geckodriver_path = r"./geckodriver.exe"

def start_browser():
    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service)
    print("Browser started successfully")
    return driver

@given('I am on the Demo Login Page')
def step_given_on_demo_login_page(context):
    context.driver = start_browser()
    context.driver.get(url)

@when('I fill the account information for account "{account}" into the Username field and the Password field')
def step_when_fill_account_information(context, account):
    if account == "standard_user":
        username = "standard_user"
        password = "secret_sauce"
    elif account == "locked_out_user":
        username = "locked_out_user"
        password = "secret_sauce"
    context.driver.find_element(By.ID, 'user-name').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)

@when('I click the Login Button')
def step_when_click_login_button(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then('I am redirected to the Demo Main Page')
def step_then_redirected_to_demo_main_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
    )

@then('I verify the App Logo exists')
def step_then_verify_app_logo_exists(context):
    logo = context.driver.find_element(By.CLASS_NAME, 'app_logo')
    assert logo is not None

@then('I verify the Error Message contains the text "{message}"')
def step_then_verify_error_message(context, message):
    error_msg = context.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
    assert message in error_msg

@given('I am on the inventory page')
def step_given_on_inventory_page(context):
    context.driver = start_browser()
    context.driver.get(url)
    username = "standard_user"
    password = "secret_sauce"
    context.driver.find_element(By.ID, 'user-name').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'login-button').click()

@when('user sorts products from low price to high price')
def step_when_sort_products(context):
    dropdown = Select(context.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    dropdown.select_by_index(2)

@when('user adds the lowest priced product')
def step_when_add_lowest_priced_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.inventory_item:first-child .btn_primary').click()

@when('user clicks on cart')
def step_when_click_cart(context):
    context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

@when('user clicks on checkout')
def step_when_click_checkout(context):
    context.driver.find_element(By.ID, 'checkout').click()

@when('user enters first name "{first_name}"')
def step_when_enter_first_name(context, first_name):
    context.driver.find_element(By.ID, 'first-name').send_keys(first_name)

@when('user enters last name "{last_name}"')
def step_when_enter_last_name(context, last_name):
    context.driver.find_element(By.ID, 'last-name').send_keys(last_name)

@when('user enters zip code "{zip_code}"')
def step_when_enter_zip_code(context, zip_code):
    context.driver.find_element(By.ID, 'postal-code').send_keys(zip_code)

@when('user clicks the Continue button')
def step_when_click_continue(context):
    context.driver.find_element(By.ID, 'continue').click()

@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def step_then_verify_total_amount(context):
    total_amount = context.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    assert "$8.63" in total_amount

@when('user clicks the Finish button')
def step_when_click_finish(context):
    context.driver.find_element(By.ID, 'finish').click()

@then('Thank You header is shown in the Checkout Complete page')
def step_then_verify_thank_you_header(context):
    header = context.driver.find_element(By.CLASS_NAME, 'complete-header').text
    assert "Thank you for your order!" in header


