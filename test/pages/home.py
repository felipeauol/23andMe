from .base_page import BasePage
from .locators import HomePageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage(BasePage):
  def goToCart(self):
    self.driver.find_element(HomePageLocators.CART_LINK).click()
