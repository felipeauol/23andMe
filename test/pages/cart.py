from .base_page import BasePage
from .locators import CartPageLocators
from .locators import CheckoutPageLocators
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

  def add_kit(self, kit_type):
    # Get number of items in cart
    item_count = len(self.driver.find_elements(*CartPageLocators.KIT_ROW))

    # Add kit
    if kit_type == 'ANCESTRY':
      add_button = self.driver.find_element(*CartPageLocators.ADD_ANCESTRY_KIT)
    elif kit_type == 'HEALTH':
      add_button = self.driver.find_element(*CartPageLocators.ADD_HEALTH_KIT)

      add_button.click()

    # Wait until kit is added
    WebDriverWait(self.driver, 5).until(
      lambda b: len(b.find_elements(*CartPageLocators.KIT_ROW)) == item_count + 1
    )

  def continue_cart(self):
    button = self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON)
    button.submit()
    WebDriverWait(self.driver, 10).until(
      EC.visibility_of_all_elements_located(CheckoutPageLocators.SHIPPING_FIELDS)
      )
