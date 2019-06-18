import pytest
from selenium import webdriver
# import time


def test_item_add_to_basket(browser):
    # time.sleep(30)
    basket = browser.find_element_by_css_selector(
        "form button.btn-add-to-basket")
    assert len(basket) > 0, "Element not found"
    print(basket.text)
