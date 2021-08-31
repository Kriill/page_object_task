from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def basket(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.product_name_should_be_equal_name_in_basket()
        self.product_price_should_be_equal_price_in_basket()

    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def product_name_should_be_equal_name_in_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_text = name.text
        name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        name_in_basket_text = name_in_basket.text
        assert name_text == name_in_basket_text, "product_name_not_equal_name_in_basket"

    def product_price_should_be_equal_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_text = price.text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        price_in_basket_text = price_in_basket.text
        assert price_text == price_in_basket_text, "product_price_not_equal_price_in_basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeare"
