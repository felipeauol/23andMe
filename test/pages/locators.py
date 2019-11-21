from selenium.webdriver.common.by import By

class BasePageLocators(object):
  PROMO_BOX_CLOSE = (By.CSS_SELECTOR, '#bx-close-inside-1072395')

class HomePageLocators(object):
  CART_LINK = (By.CSS_SELECTOR, "a[data-testid='cart-icon-link']")

class CartPageLocators(object):
  ADD_ANCESTRY_KIT = (By.ID, 'button-add-ancestry-kit')
  ADD_HEALTH_KIT = (By.ID, 'button-add-health-kit')
  KIT_ROW = (By.CSS_SELECTOR, 'li div.cart-item-row')
  CHECKOUT_BUTTON = (By.CSS_SELECTOR, "form input[value='checkout']")

class CheckoutPageLocators(object):
  SHIPPING_FIELDS = (By.CSS_SELECTOR, 'form *.spc-input')
  FIRST_NAME = (By.ID, 'js-shipping-firstname')
  LAST_NAME = (By.ID, 'js-shipping-lastname')
  COMPANY = (By.ID, 'js-shipping-company')
  ADDRESS = (By.ID, 'js-shipping-address')
  ADDRESS_2 = (By.ID, 'js-shipping-address2')
  CITY = (By.ID, 'js-shipping-city')
  STATE = (By.ID, 'js-shipping-state')
  ZIP_CODE = (By.ID, 'js-shipping-zip')
  EMAIL = (By.ID, 'js-shipping-email')
  PHONE = (By.ID, 'js-shipping-phone')
  SHIPPING_BUTTON = (By.CSS_SELECTOR, '[data-stor-id="spc-address-continue-button"]')
  ADDRESS_VERIFICATION_MODAL = (By.CLASS_NAME, 'spc-verification-p')
  SHIP_TO_VERIFIED_BUTTON = (By.CSS_SELECTOR, "[data-stor-id='spc-ship-verified-address-button']")
  SHIPPING_METHODS = (By.CSS_SELECTOR, ".spc-shipping .spc-shipping-method")
  CONTINUE_TO_BILLING = (By.CSS_SELECTOR, "[data-stor-id='spc-shipping-method-continue-button']")
  BILLING_ADDRESS = (By.CSS_SELECTOR, "[data-stor-id='spc-billing-address']")

