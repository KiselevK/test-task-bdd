from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')


def take_screenshot(browser, screenshot_name: str) -> None:
    filename = f"output/{screenshot_name}.png"
    browser.save_screenshot(filename)


@given("I am on the DemoBlaze homepage")
def step_impl(context):
    context.browser = webdriver.Chrome(options=options)
    context.browser.set_window_size(1920, 1080)
    context.browser.get("https://www.demoblaze.com")
    sleep(2)
    take_screenshot(context.browser, "1 DemoBlaze homepage")


@when('I select the "{product_name}"')
def step_impl(context, product_name):
    context.browser.find_element(By.XPATH, f'//*[text() = "{product_name}"]').click()
    sleep(2)
    take_screenshot(context.browser, f"2 {product_name}")


@when("I add the product to the cart")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[text() = 'Add to cart']").click()
    sleep(2)
    alert = context.browser.switch_to.alert
    alert.accept()
    sleep(2)


@when("I proceed to the cart")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[text() = 'Cart']").click()
    sleep(3)
    take_screenshot(context.browser, "4 Cart page")


@when("I place an order")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[text() = 'Place Order']").click()
    sleep(3)


@when(
    'I fill in the order form with Name "{name}", Country "{country}", City "{city}", Credit Card "{credit_card}", Month "{month}", Year "{year}"'
)
def step_impl(context, name, country, city, credit_card, month, year):
    context.browser.find_element(By.ID, "name").send_keys(name)
    context.browser.find_element(By.ID, "country").send_keys(country)
    context.browser.find_element(By.ID, "city").send_keys(city)
    context.browser.find_element(By.ID, "card").send_keys(credit_card)
    context.browser.find_element(By.ID, "month").send_keys(month)
    context.browser.find_element(By.ID, "year").send_keys(year)
    sleep(3)
    take_screenshot(context.browser, "5 Order_form")


@when("I confirm the purchase")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[text() = 'Purchase']").click()
    sleep(3)
    take_screenshot(context.browser, "6 Purchase")


@then("I should see the confirmation of the purchase")
def step_impl(context):
    sleep(1)
    assert "Thank you for your purchase!" in context.browser.page_source
    context.browser.find_element(By.XPATH, "//*[text() = 'OK']").click()
    sleep(1)
    context.browser.quit()
