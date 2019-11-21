from .base_page import BasePage
from .locators import CheckoutPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):

  def first_name(self, value):
    self.driver.find_element(*CheckoutPageLocators.FIRST_NAME).send_keys(value)

  def last_name(self, value):
    self.driver.find_element(*CheckoutPageLocators.LAST_NAME).send_keys(value)

  def company(self, value):
    self.driver.find_element(*CheckoutPageLocators.COMPANY).send_keys(value)

  def address(self, value):
    self.driver.find_element(*CheckoutPageLocators.ADDRESS).send_keys(value)

  def address_2(self, value):
    self.driver.find_element(*CheckoutPageLocators.ADDRESS_2).send_keys(value)

  def city(self, value):
    self.driver.find_element(*CheckoutPageLocators.CITY).send_keys(value)

  def state(self, value):
    Select(self.driver.find_element(*CheckoutPageLocators.STATE)).select_by_value(value)

  def zip_code(self, value):
    self.driver.find_element(*CheckoutPageLocators.ZIP_CODE).send_keys(value)

  def email(self, value):
    self.driver.find_element(*CheckoutPageLocators.EMAIL).send_keys(value)

  def phone(self, value):
    self.driver.find_element(*CheckoutPageLocators.PHONE).send_keys(value)

  def continue_checkout(self):
    self.driver.find_element(*CheckoutPageLocators.SHIPPING_BUTTON).click()
  
  def continue_shipping(self):
    self.driver.find_element(*CheckoutPageLocators.SHIPPING_BUTTON).click()

  def address_verified(self):
    verification_success_modal = 'We verified your shipping address and found an exact match'
    
    summary = WebDriverWait(self.driver, 5).until( lambda x:
      x.find_element(*CheckoutPageLocators.ADDRESS_VERIFICATION_MODAL)
    ).text

    if verification_success_modal not in summary:
      return False
    else:
      return True

  def close_verification_modal(self):
    wait = WebDriverWait(self.driver, 5)
    wait.until(EC.element_to_be_clickable(CheckoutPageLocators.SHIP_TO_VERIFIED_BUTTON))
    self.driver.find_element(*CheckoutPageLocators.SHIP_TO_VERIFIED_BUTTON).click()

  def select_express_shipping(self):
    WebDriverWait(self.driver, 5).until(
      EC.element_to_be_clickable(CheckoutPageLocators.SHIPPING_METHODS)
    )
    self.driver.find_elements(*CheckoutPageLocators.SHIPPING_METHODS).pop().click()
  
  def continue_billing(self):
    self.driver.find_element(*CheckoutPageLocators.CONTINUE_TO_BILLING).click()

  def billing_address_present(self):
    billing_name = 'Felipe Oliveira'
    summary = WebDriverWait(self.driver, 5).until( lambda x:
      x.find_element(*CheckoutPageLocators.BILLING_ADDRESS)
    ).text

    if billing_name not in summary:
      return False
    else:
      return True
